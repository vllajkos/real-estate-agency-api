"""Routes for advertisement"""
from fastapi import APIRouter, Depends

from app.advertisements.controller import AdvertisementController
from app.advertisements.models.hardcoded_data import (
    AdStatus,
    AdStatusUserStat,
    EmployeeAdStatus,
    SortByPrice,
    TypeOfAd,
    UserAdStatus,
)
from app.advertisements.schemas import AdvertisementSchemaIn, AdvertisementSchemaOut, FilterSchemaIn
from app.users.controller import JWTBearer

advertisement_router = APIRouter(prefix="/api/advertisement", tags=["Advertisement"])


@advertisement_router.post(
    "/create-sale-ad", response_model=AdvertisementSchemaOut, dependencies=[Depends(JWTBearer("user"))]
)
def create_sale_advertisement(advertisement: AdvertisementSchemaIn):
    """Create sale advertisement"""
    return AdvertisementController.create(
        type_of_ad=TypeOfAd.SALE.value,
        price=advertisement.price,
        description=advertisement.description,
        property_id=advertisement.property_id,
        client_id=advertisement.client_id,
    )


@advertisement_router.post(
    "/create-rent-ad", response_model=AdvertisementSchemaOut, dependencies=[Depends(JWTBearer("user"))]
)
def create_rent_advertisement(advertisement: AdvertisementSchemaIn):
    """Create rent advertisement"""
    return AdvertisementController.create(
        type_of_ad=TypeOfAd.RENT.value,
        price=advertisement.price,
        description=advertisement.description,
        property_id=advertisement.property_id,
        client_id=advertisement.client_id,
    )


@advertisement_router.get(
    "/get-all-on-pending-for-employee",
    response_model=list[AdvertisementSchemaOut],
    dependencies=[Depends(JWTBearer("superuser"))],
)
def get_all_ads_on_pending_for_employee_id(employee_id: str):
    """Get all ads on pending for employee id"""
    return AdvertisementController.get_all_on_pending_for_employee_id(employee_id=employee_id)


@advertisement_router.get("/get-all-active-ads-for-client-id/{client_id}", response_model=list[AdvertisementSchemaOut])
def get_all_active_for_client_id(client_id: str):
    """Get all active ads for certain user"""
    return AdvertisementController.get_all_active_for_client_id(client_id=client_id)


@advertisement_router.get("/get-active-advertisement-by-id/{advertisement_id}", response_model=AdvertisementSchemaOut)
def get_active_advertisement_by_id(advertisement_id: str):
    """Get active advertisements by id"""
    return AdvertisementController.get_active_advertisement_by_id(advertisement_id=advertisement_id)


@advertisement_router.get("/get-all-active-ads", response_model=list[AdvertisementSchemaOut])
def get_all_active_ads():
    """Get all active ads"""
    return AdvertisementController.get_all_active_ads()


@advertisement_router.get(
    "/get-all-active-ads-by-type-sorted/{type_of_ad}", response_model=list[AdvertisementSchemaOut]
)
def get_all_active_ads_by_type_of_ad_sorted(type_of_ad: TypeOfAd, sort_: SortByPrice):
    """Get all active ads by type of ad, sorted by price"""
    return AdvertisementController.get_all_active_ads_by_type_of_ad_sorted(
        type_of_ad=type_of_ad.value, sort_=sort_.value
    )


@advertisement_router.get(
    "/get-all-active-ads-by-type-of-ad-and-type-of-property", response_model=list[AdvertisementSchemaOut]
)
def get_all_active_ads_by_type_of_ad_and_type_of_property_id(type_of_ad: TypeOfAd, type_of_property_id: str):
    """Get all active ads by type of ad and type of property id"""
    return AdvertisementController.get_all_active_ads_by_type_of_ad_and_type_of_property_id(
        type_of_ad=type_of_ad.value, type_of_property_id=type_of_property_id
    )


@advertisement_router.get("/get-all-by-ad-and-property-types-and-city", response_model=list[AdvertisementSchemaOut])
def get_all_by_ad_and_property_types_and_city(type_of_ad: TypeOfAd, type_of_property_id: str, city: str):
    """Get all ads by type of ad, type of property and city"""
    return AdvertisementController.get_all_by_ad_and_property_types_and_city(
        type_of_ad=type_of_ad.value, type_of_property_id=type_of_property_id, city=city
    )


@advertisement_router.post("/filter-by-parameters", response_model=list[AdvertisementSchemaOut])
def get_by_filter_parameters(filter_param: FilterSchemaIn):
    """Get all active ads by optional search parameters"""
    return AdvertisementController.get_by_filter_parameters(
        type_of_ad=filter_param.type_of_ad,
        min_price=filter_param.min_price,
        max_price=filter_param.max_price,
        municipality=filter_param.municipality,
        city=filter_param.city,
        country=filter_param.country,
        min_square_meters=filter_param.min_square_meters,
        max_square_meters=filter_param.max_square_meters,
        type_of_property_id=filter_param.type_of_property_id,
        feature_id_list=filter_param.feature_id_list,
        features_id_operator_value_list=filter_param.features_id_operator_value_list,
    )


@advertisement_router.put(
    "/update-ad-status", response_model=AdvertisementSchemaOut, dependencies=[Depends(JWTBearer("user"))]
)
def update_ad_status_as_user(clients_id: str, advertisement_id: str, status: UserAdStatus):
    """Update ad status as user"""
    return AdvertisementController.update_ad_status(
        clients_id=clients_id, advertisement_id=advertisement_id, status=status.value
    )


@advertisement_router.put(
    "/update-ad-status-to-expired",
    response_model=list[AdvertisementSchemaOut],
    dependencies=[Depends(JWTBearer("superuser"))],
)
def update_ad_status_to_expired():
    """When called automatically changes status for active ads to expired if they are active more than 30 days"""
    return AdvertisementController.update_ad_status_to_expired()


@advertisement_router.put(
    "/update-pending-status", response_model=AdvertisementSchemaOut, dependencies=[Depends(JWTBearer("superuser"))]
)
def update_pending_status(advertisement_id: str, status: EmployeeAdStatus):
    """Updates pending status for ad by employee"""
    return AdvertisementController.update_pending_status(advertisement_id=advertisement_id, status=status.value)


@advertisement_router.get(
    "/get-stats-for-ads-for-users", response_model=None, dependencies=[Depends(JWTBearer("user"))]
)
def get_stats_of_ads_for_user(
    status: AdStatusUserStat,
    type_of_ad: TypeOfAd,
    type_of_property_id: str,
    city: str = None,
    start_date: str = None,
    end_date: str = None,
):
    """Get number of active or sold/rented ads for given parameters with
    average property price and avg square meter price for users"""
    return AdvertisementController.get_stats(
        type_of_ad=type_of_ad,
        status=status,
        type_of_property_id=type_of_property_id,
        city=city,
        start_date=start_date,
        end_date=end_date,
    )


@advertisement_router.get(
    "/get-stats-on-avg-price-for-users", response_model=None, dependencies=[Depends(JWTBearer("user"))]
)
def get_stat_on_avg_price_by_city(
    status: AdStatusUserStat,
    type_of_ad: TypeOfAd,
    type_of_property_id: str = None,
    start_date: str = None,
    end_date: str = None,
):
    """
    It gets the stats on average price of square meter for city for active or sold/rented properties
    by search parameters for users
    """
    return AdvertisementController.get_stat_on_avg_price_by_city(
        type_of_ad=type_of_ad,
        status=status,
        type_of_property_id=type_of_property_id,
        start_date=start_date,
        end_date=end_date,
    )


@advertisement_router.get("/get-stats-for-ads", response_model=None, dependencies=[Depends(JWTBearer("superuser"))])
def get_stats_of_ads(
    status: AdStatus,
    type_of_ad: TypeOfAd = None,
    type_of_property_id: str = None,
    city: str = None,
    start_date: str = None,
    end_date: str = None,
):
    """Get number of ads for given parameters including full range of statuses available to filter from
    with average property price and avg square meter price for employee"""
    return AdvertisementController.get_stats(
        type_of_ad=type_of_ad,
        status=status,
        type_of_property_id=type_of_property_id,
        city=city,
        start_date=start_date,
        end_date=end_date,
    )


@advertisement_router.get(
    "/get-stats-on-avg-price", response_model=None, dependencies=[Depends(JWTBearer("superuser"))]
)
def get_stat_on_avg_price_by_city(
    status: AdStatus,
    type_of_ad: TypeOfAd = None,
    type_of_property_id: str = None,
    start_date: str = None,
    end_date: str = None,
):
    """
    With all available statuses to choose from, gets the stats on average price of square meter
     for city by search parameters for employee
    """
    return AdvertisementController.get_stat_on_avg_price_by_city(
        type_of_ad=type_of_ad,
        status=status,
        type_of_property_id=type_of_property_id,
        start_date=start_date,
        end_date=end_date,
    )
