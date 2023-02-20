from datetime import date

from fastapi import APIRouter

from app.advertisements.controller import AdvertisementController
from app.advertisements.models.hardcoded_data import TypeOfAd, UserAdStatus, SortByPrice, EmployeeAdStatus
from app.advertisements.schemas import AdvertisementSchemaIn, AdvertisementSchemaOut, FilterSchemaIn

advertisement_router = APIRouter(prefix="/api/advertisement", tags=["Advertisement"])


@advertisement_router.post("/create-sale-ad", response_model=AdvertisementSchemaOut)
def create_sale_advertisement(advertisement: AdvertisementSchemaIn):
    return AdvertisementController.create(type_of_ad=TypeOfAd.SALE.value,
                                          price=advertisement.price,
                                          description=advertisement.description,
                                          property_id=advertisement.property_id,
                                          client_id=advertisement.client_id)


@advertisement_router.post("/create-rent-ad", response_model=AdvertisementSchemaOut)
def create_rent_advertisement(advertisement: AdvertisementSchemaIn):
    return AdvertisementController.create(type_of_ad=TypeOfAd.RENT.value,
                                          price=advertisement.price,
                                          description=advertisement.description,
                                          property_id=advertisement.property_id,
                                          client_id=advertisement.client_id)


@advertisement_router.get("/get-all-on-pending-for-employee",
                          response_model=list[AdvertisementSchemaOut])
def get_all_ads_on_pending_for_employee_id(employee_id: str):
    return AdvertisementController.get_all_od_pending_for_employee_id(employee_id=employee_id)


@advertisement_router.get("/get-active-advertisement-by-id/{advertisement_id}",
                          response_model=AdvertisementSchemaOut)
def get_active_advertisement_by_id(advertisement_id: str):
    return AdvertisementController.get_active_advertisement_by_id(advertisement_id=advertisement_id)


@advertisement_router.get("/get-all-active-ads", response_model=list[AdvertisementSchemaOut])
def get_all_active_ads():
    return AdvertisementController.get_all_active_ads()


@advertisement_router.get("/get-all-active-ads-by-type-sorted/{type_of_ad}",
                          response_model=list[AdvertisementSchemaOut])
def get_all_active_ads_by_type_of_ad_sorted(type_of_ad: TypeOfAd, sort_: SortByPrice):
    return AdvertisementController.get_all_active_ads_by_type_of_ad_sorted(type_of_ad=type_of_ad.value,
                                                                           sort_=sort_.value)


@advertisement_router.get("/get-all-active-ads-by-type-of-ad-and-type-of-property",
                          response_model=list[AdvertisementSchemaOut])
def get_all_active_ads_by_type_of_ad_and_type_of_property_id(type_of_ad: TypeOfAd, type_of_property_id: str):
    return AdvertisementController.get_all_active_ads_by_type_of_ad_and_type_of_property_id(
        type_of_ad=type_of_ad.value, type_of_property_id=type_of_property_id)


@advertisement_router.get("/get-all-by-ad-and-property-types-and-city", response_model=list[AdvertisementSchemaOut])
def get_all_by_ad_and_property_types_and_city(type_of_ad: TypeOfAd, type_of_property_id: str, city: str):
    return AdvertisementController.get_all_by_ad_and_property_types_and_city(type_of_ad=type_of_ad.value,
                                                                             type_of_property_id=type_of_property_id,
                                                                             city=city)


@advertisement_router.post("/filter-by-parameters", response_model=list[AdvertisementSchemaOut])
def get_by_filter_parameters(filter_param: FilterSchemaIn):
    return AdvertisementController.get_by_filter_parameters(type_of_ad=filter_param.type_of_ad,
                                                            min_price=filter_param.min_price,
                                                            max_price=filter_param.max_price,
                                                            municipality=filter_param.municipality,
                                                            city=filter_param.city,
                                                            country=filter_param.country,
                                                            min_square_meters=filter_param.min_square_meters,
                                                            max_square_meters=filter_param.max_square_meters,
                                                            type_of_property_id=filter_param.type_of_property_id,
                                                            feature_id_list=filter_param.feature_id_list,
                                                            features_id_operator_value_list=
                                                            filter_param.features_id_operator_value_list)


@advertisement_router.put("/update-ad-status", response_model=AdvertisementSchemaOut)
def update_ad_status_as_user(advertisement_id: str, status: UserAdStatus):
    return AdvertisementController.update_ad_status(advertisement_id=advertisement_id, status=status.value)


@advertisement_router.put("/update-ad-status-to-expired", response_model=list[AdvertisementSchemaOut])
def update_ad_status_to_expired():
    return AdvertisementController.update_ad_status_to_expired()


@advertisement_router.put("/update-pending-status", response_model=AdvertisementSchemaOut)
def update_pending_status(advertisement_id: str, status: EmployeeAdStatus):
    return AdvertisementController.update_pending_status(advertisement_id=advertisement_id, status=status.value)


@advertisement_router.get("/get-stats-of-successful-ads", response_model=None)
def get_stats_of_successful_ads(type_of_ad: TypeOfAd = None, type_of_property_id: str = None, city: str = None,
                                start_date: str = None, end_date: str = None):
    type_of_ad = None if type_of_ad is None else type_of_ad.value
    return AdvertisementController.get_stats(type_of_ad=type_of_ad, type_of_property_id=type_of_property_id,
                                             city=city, start_date=start_date, end_date=end_date)
