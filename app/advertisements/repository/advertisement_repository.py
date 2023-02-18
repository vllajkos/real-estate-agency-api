from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload

from app.advertisements.models import Advertisement
from app.advertisements.models.advertisements import AdStatus, TypeOfAd
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

    def get_advertisements_by_property_id(self, property_id: str):
        # I used options(joined load) to load property object to advertisement in a single query rather than access them
        # separately
        return self.db.query(Advertisement).join(Property).options(joinedload(Advertisement.property)).\
            filter(Advertisement.property_id == property_id).all()

    def get_all_active_ads(self):
        return self.db.query(Advertisement).join(Property).options(joinedload(Advertisement.property)).\
            filter(Advertisement.status == AdStatus.ACTIVE.value).all()

    def get_all_active_ads_by_type_of_ad(self, type_of_ad: str):
        return self.db.query(Advertisement).join(Property).options(joinedload(Advertisement.property)).\
            filter((Advertisement.type_of_ad == type_of_ad) & (Advertisement.status == AdStatus.ACTIVE.value)).all()

    def get_all_active_ads_by_type_of_ad_and_type_of_property_id(self, type_of_ad: str, type_of_property_id: str):
        return self.db.query(Advertisement).join(Property).options(joinedload(Advertisement.property)). \
            filter((Advertisement.type_of_ad == type_of_ad) & (Property.type_of_property_id == type_of_property_id) &
                   (Advertisement.status == AdStatus.ACTIVE.value)).all()

    def get_all_by_ad_and_property_types_and_city(self, type_of_ad: str, type_of_property_id: str, city: str):
        return self.db.query(Advertisement).join(Property).options(joinedload(Advertisement.property)).\
            filter((Advertisement.type_of_ad == type_of_ad) & (Property.type_of_property_id == type_of_property_id) &
                   (Property.city == city) & (Advertisement.status == AdStatus.ACTIVE.value)).all()
