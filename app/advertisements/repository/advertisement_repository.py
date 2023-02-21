from datetime import timedelta, date

from sqlalchemy import desc, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload

from app.advertisements.exceptions import MinMaxPriceException, AdvertisementNoLongerActiveException, \
    AdvertisementIdDoesntExistException, NoExpiredAdsException, AdNotPendingException, EnterValidStartEndDateException
from app.advertisements.models import Advertisement
from app.advertisements.models.hardcoded_data import EXPIRES_IN_DAYS, AdStatus, SortByPrice
from app.properties.models import Property


class AdvertisementRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, type_of_ad: str, price: float, description: str, property_id: str, client_id: str,
               employee_id: str):
        try:
            advertisement = Advertisement(type_of_ad=type_of_ad, price=price, description=description,
                                          property_id=property_id, client_id=client_id, employee_id=employee_id)
            self.db.add(advertisement)
            self.db.commit()
            self.db.refresh(advertisement)
            return advertisement
        except IntegrityError as exc:
            raise exc

    def get_all_on_pending_for_employee_id(self, employee_id: str):
        return self.db.query(Advertisement).filter((Advertisement.employee_id == employee_id) &
                                                   (Advertisement.status == AdStatus.PENDING.value)).all()

    def get_ad_by_id(self, advertisement_id: str):
        ad = self.db.query(Advertisement).filter(Advertisement.id == advertisement_id).first()
        if ad:
            return ad
        raise AdvertisementIdDoesntExistException

    def get_active_advertisement_by_id(self, advertisement_id: str):
        ad = self.get_ad_by_id(advertisement_id=advertisement_id)
        if ad.status == AdStatus.ACTIVE.value:
            return ad
        raise AdvertisementNoLongerActiveException

    def get_advertisements_by_property_id(self, property_id: str):
        # I used options(joined load) to load property object to advertisement in a single query rather than to
        # access them separately
        return self.db.query(Advertisement).join(Property).options(joinedload(Advertisement.property)). \
            filter(Advertisement.property_id == property_id).all()

    def get_active_advertisements_by_property_id_and_type_of_ad_and_price(self, min_price: float, max_price: float,
                                                                          properties_ids_list: list[str],
                                                                          type_of_ad: str = None):
        query = self.db.query(Advertisement).join(Property).options(joinedload(Advertisement.property))
        # if type_of_ad is provided
        if type_of_ad:
            query = query.filter(Advertisement.type_of_ad == type_of_ad)
        if min_price and max_price:
            if min_price > max_price:
                raise MinMaxPriceException
            query = query.filter(Advertisement.price.between(min_price, max_price))
        elif min_price:
            query = query.filter(Advertisement.price > min_price)
        elif max_price:
            query = query.filter(Advertisement.price < max_price)
        if properties_ids_list:
            query = query.filter(Advertisement.property_id.in_(properties_ids_list))
        return query.filter(Advertisement.status == AdStatus.ACTIVE.value).all()

    def get_all_active_ads(self):
        return self.db.query(Advertisement).join(Property).options(joinedload(Advertisement.property)). \
            filter(Advertisement.status == AdStatus.ACTIVE.value).all()

    def get_all_active_ads_by_type_of_ad_sorted(self, type_of_ad: str, sort_: str):
        query = self.db.query(Advertisement).join(Property).options(joinedload(Advertisement.property)) \
            .filter((Advertisement.type_of_ad == type_of_ad) & (Advertisement.status == AdStatus.ACTIVE.value))
        if sort_ == SortByPrice.LOW.value:
            query = query.order_by(Advertisement.price.asc())
        elif sort_ == SortByPrice.HIGH.value:
            query = query.order_by(desc(Advertisement.price))
        return query.all()

    def get_all_active_ads_by_type_of_ad_and_type_of_property_id(self, type_of_ad: str, type_of_property_id: str):
        return self.db.query(Advertisement).join(Property).options(joinedload(Advertisement.property)). \
            filter((Advertisement.type_of_ad == type_of_ad) & (Property.type_of_property_id == type_of_property_id) &
                   (Advertisement.status == AdStatus.ACTIVE.value)).all()

    def get_all_by_ad_and_property_types_and_city(self, type_of_ad: str, type_of_property_id: str, city: str):
        return self.db.query(Advertisement).join(Property).options(joinedload(Advertisement.property)). \
            filter((Advertisement.type_of_ad == type_of_ad) & (Property.type_of_property_id == type_of_property_id) &
                   (Property.city == city) & (Advertisement.status == AdStatus.ACTIVE.value)).all()

    def get_clients_id_by_advertisement_id(self, advertisement_id: str):
        return self.db.query(Advertisement.client_id).filter(Advertisement.id == advertisement_id).first()

    def update_ad_status(self, advertisement_id: str, status: str):
        try:
            ad = self.get_active_advertisement_by_id(advertisement_id=advertisement_id)
            ad.status = status
            ad.status_date = date.today()
            self.db.add(ad)
            self.db.commit()
            self.db.refresh(ad)
            return ad
        except Exception as exc:
            raise exc

    def update_ad_status_to_expired(self):
        try:
            end_date = date.today() - timedelta(days=EXPIRES_IN_DAYS)
            ads_list = self.db.query(Advertisement).filter((Advertisement.status == AdStatus.ACTIVE.value) &
                                                           (Advertisement.status_date <= end_date)).all()
            if ads_list:
                expired_ads = []
                for ad in ads_list:
                    ad.status = AdStatus.EXPIRED.value
                    ad.status_date = date.today()
                    self.db.add(ad)
                    self.db.commit()
                    self.db.refresh(ad)
                    expired_ads.append(ad)
                return expired_ads
            raise NoExpiredAdsException
        except Exception as exc:
            raise exc

    def update_pending_status(self, advertisement_id: str, status: str):
        try:
            ad = self.get_ad_by_id(advertisement_id=advertisement_id)
            if ad.status == AdStatus.PENDING.value:
                ad.status = status
                ad.status_date = date.today()
                self.db.add(ad)
                self.db.commit()
                self.db.refresh(ad)
                return ad
            raise AdNotPendingException
        except Exception as exc:
            raise exc

    def get_stats(self, type_of_ad: str, type_of_property_id: str, city: str, start_date: date, end_date: date):
        query = self.db.query(func.count(Advertisement.id),
                              func.avg(Advertisement.price),
                              func.avg(Advertisement.price) / func.avg(Property.square_meters)).join(Property). \
            filter(Advertisement.status == AdStatus.SOLD_RENTED.value)

        if type_of_ad:
            query = query.filter(Advertisement.type_of_ad == type_of_ad)
        if type_of_property_id:
            query = query.filter(Property.type_of_property_id == type_of_property_id)
        if city:
            query = query.filter(Property.city == city)
        if start_date and end_date:
            if start_date > end_date:
                raise EnterValidStartEndDateException
            query = query.filter(Advertisement.status_date.between(start_date, end_date))
        elif start_date:
            query = query.filter(Advertisement.status_date > start_date)
        elif end_date:
            query = query.filter(Advertisement.status_date < end_date)
            # (Advertisement.status == AdStatus.SOLD_RENTED.value) &
            # (Advertisement.start_date.between(start_date, end_date)) &
            # (Advertisement.type_of_ad == type_of_ad)).first()

        # result is a tuple of two elements, first is an ads number second is an average price of property
        return query.first()
