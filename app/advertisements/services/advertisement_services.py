from app.advertisements.exceptions import TypeOfAdExistsForPropertyException
from app.advertisements.models.advertisements import AdStatus, TypeOfAd
from app.advertisements.repository import AdvertisementRepository
from app.db import SessionLocal
from app.properties.services import PropertyService
from app.users.services import ClientService, EmployeeService


class AdvertisementService:

    @staticmethod
    def create(type_of_ad: str, price: float, description: str, property_id: str, client_id: str):
        try:
            with SessionLocal() as db:
                # checks if property id exist if not raises an exception
                PropertyService.get_property_by_id(property_id=property_id)
                # checks if client id exists if not raises an exception
                ClientService.get_client_by_id(client_id=client_id)
                ad_repository = AdvertisementRepository(db)
                # returns a list for all advertisements matching property id
                ad_list = ad_repository.get_advertisements_by_property_id(property_id=property_id)
                for ad in ad_list:
                    # for all found ads for property id, checks if there is an active ad with same type of ad
                    # if exists raises an exception
                    if ad.type_of_ad == type_of_ad and ad.status == AdStatus.ACTIVE.value:
                        raise TypeOfAdExistsForPropertyException
                # if everything is ok, ad can be created
                # random employee's id is passed to an ad for ad to be revised and approved
                employee = EmployeeService.get_random_employee()
                return ad_repository.create(type_of_ad=type_of_ad, price=price, description=description,
                                            property_id=property_id, client_id=client_id, employee_id=employee.id)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_active_ads():
        try:
            with SessionLocal() as db:
                ad_repository = AdvertisementRepository(db)
                return ad_repository.get_all_active_ads()
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_active_ads_by_type_of_ad(type_of_ad: str):
        try:
            with SessionLocal() as db:
                ad_repository = AdvertisementRepository(db)
                return ad_repository.get_all_active_ads_by_type_of_ad(type_of_ad=type_of_ad)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_active_ads_by_type_of_ad_and_type_of_property_id(type_of_ad: str, type_of_property_id: str):
        try:
            with SessionLocal() as db:
                ad_repository = AdvertisementRepository(db)
                return ad_repository.get_all_active_ads_by_type_of_ad_and_type_of_property_id(
                    type_of_ad=type_of_ad, type_of_property_id=type_of_property_id)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_by_ad_and_property_types_and_city(type_of_ad: str, type_of_property_id: str, city: str):
        try:
            with SessionLocal() as db:
                ad_repository = AdvertisementRepository(db)
                return ad_repository.get_all_by_ad_and_property_types_and_city(type_of_ad=type_of_ad,
                                                                               type_of_property_id=type_of_property_id,
                                                                               city=city)
        except Exception as exc:
            raise exc
