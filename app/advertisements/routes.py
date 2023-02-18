from fastapi import APIRouter

from app.advertisements.controller import AdvertisementController
from app.advertisements.models.advertisements import TypeOfAd
from app.advertisements.schemas import AdvertisementSchemaIn, AdvertisementSchemaOut

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


@advertisement_router.get("/get-all-active-ads", response_model=list[AdvertisementSchemaOut])
def get_all_active_ads():
    return AdvertisementController.get_all_active_ads()


@advertisement_router.get("/get-all-active-ads-by-type/{type_of_ad}", response_model=list[AdvertisementSchemaOut])
def get_all_active_ads_by_type_of_ad(type_of_ad: TypeOfAd):
    return AdvertisementController.get_all_active_ads_by_type_of_ad(type_of_ad=type_of_ad.value)


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

