"""Service layer for advertisements"""
from datetime import datetime
from typing import Any

from app.advertisements.exceptions import (
    AdNotFoundByFilteredParametersException,
    EnterValidDateFormatException,
    NoAdsForClientIdException,
    NoPendingAdsException,
    NotAuthorizedException,
    PendingApprovalException,
    TypeOfAdExistsForPropertyException,
)
from app.advertisements.models import Advertisement
from app.advertisements.models.hardcoded_data import AdStatus
from app.advertisements.repository import AdvertisementRepository
from app.db import SessionLocal
from app.properties.services import PropertyHasFeatureService, PropertyService, TypeOfPropertyService
from app.users.services import ClientService, EmployeeService


class AdvertisementService:
    """Class containing Advertisement service methods"""

    @staticmethod
    def create(type_of_ad: str, price: float, description: str, property_id: str, client_id: str) -> Advertisement:
        """Creates Advertisement"""
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
                    # for all found ads for property id, checks if there is an ad pending approval with same type of ad
                    # if exists raises an exception
                    if ad.type_of_ad == type_of_ad and ad.status == AdStatus.PENDING.value:
                        raise PendingApprovalException
                # if everything is ok, ad can be created
                # random employee's id is passed to an ad for ad to be revised and approved
                employee = EmployeeService.get_random_employee()
                return ad_repository.create(
                    type_of_ad=type_of_ad,
                    price=price,
                    description=description,
                    property_id=property_id,
                    client_id=client_id,
                    employee_id=employee.id,
                )
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_on_pending_for_employee_id(employee_id: str) -> list:
        """Get all ads on pending for employee id"""
        try:
            with SessionLocal() as db:
                ad_repository = AdvertisementRepository(db)
                ads = ad_repository.get_all_on_pending_for_employee_id(employee_id=employee_id)
                if ads:
                    return ads
                raise NoPendingAdsException
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_active_for_client_id(client_id: str) -> list:
        """
        It gets all active ads for a client id
        """
        try:
            with SessionLocal() as db:
                ClientService.get_client_by_id(client_id=client_id)
                ad_repository = AdvertisementRepository(db)
                ads = ad_repository.get_all_active_for_client_id(client_id=client_id)
                if ads:
                    return ads
                raise NoAdsForClientIdException
        except Exception as exc:
            raise exc

    @staticmethod
    def get_active_advertisement_by_id(advertisement_id: str) -> Advertisement:
        """
        It gets an active advertisement by id
        """
        try:
            with SessionLocal() as db:
                ad_repository = AdvertisementRepository(db)
                return ad_repository.get_active_advertisement_by_id(advertisement_id=advertisement_id)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_active_ads() -> list:
        """
        It gets all active ads from the database
        """
        try:
            with SessionLocal() as db:
                ad_repository = AdvertisementRepository(db)
                return ad_repository.get_all_active_ads()
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_active_ads_by_type_of_ad_sorted(type_of_ad: str, sort_: str) -> list:
        """
        It gets all active ads by type of ad and sorts them by the sort parameter
        """
        try:
            with SessionLocal() as db:
                ad_repository = AdvertisementRepository(db)
                return ad_repository.get_all_active_ads_by_type_of_ad_sorted(type_of_ad=type_of_ad, sort_=sort_)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_active_ads_by_type_of_ad_and_type_of_property_id(type_of_ad: str, type_of_property_id: str) -> list:
        """
        It gets all active ads by type of ad and type of property id
        """
        try:
            with SessionLocal() as db:
                ad_repository = AdvertisementRepository(db)
                return ad_repository.get_all_active_ads_by_type_of_ad_and_type_of_property_id(
                    type_of_ad=type_of_ad, type_of_property_id=type_of_property_id
                )
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_by_ad_and_property_types_and_city(type_of_ad: str, type_of_property_id: str, city: str) -> list:
        """
        It gets all the advertisements by type of ad, type of property and city
        """
        try:
            with SessionLocal() as db:
                ad_repository = AdvertisementRepository(db)
                return ad_repository.get_all_by_ad_and_property_types_and_city(
                    type_of_ad=type_of_ad, type_of_property_id=type_of_property_id, city=city
                )
        except Exception as exc:
            raise exc

    @staticmethod
    def get_by_filter_parameters(
        type_of_ad: str,
        min_price: float,
        max_price: float,
        municipality: str,
        city: str,
        country: str,
        min_square_meters: float,
        max_square_meters: float,
        type_of_property_id: str,
        feature_id_list: list[str],
        features_id_operator_value_list: list[tuple[str, str, int]],
    ) -> list:
        """Returns active advertisements by filter parameters"""
        try:
            with SessionLocal() as db:
                properties = []
                # returns found property ids if they satisfy search parameters or raises an exception if non found
                # without search parameters never returns empty list except where there are no ads
                properties_1 = PropertyService.get_properties_ids_by_filter_parameters(
                    municipality=municipality,
                    city=city,
                    country=country,
                    min_square_meters=min_square_meters,
                    max_square_meters=max_square_meters,
                    type_of_property_id=type_of_property_id,
                )
                # if there are provided features to search for
                properties_2 = []
                if feature_id_list:
                    # returns found property ids if they satisfy search parameters or raises an exception if non found
                    properties_2 = PropertyHasFeatureService.get_properties_ids_by_filter_parameters(
                        features_id_list=feature_id_list
                    )
                # intersection of properties_1 and properties_2 are ids found which satisfy both conditions
                # since they are a single tuples ,id_tuple[0] is id and here I make a list of properties ids
                # properties 3 is for features with additional value if provided enters a function
                properties_3 = []
                if features_id_operator_value_list:
                    properties_3 = PropertyHasFeatureService.get_properties_ids_by_feature_value(
                        features_id_operator_value_list=features_id_operator_value_list
                    )
                if properties_2 and properties_3:
                    # intersection of properties_1 and properties_2 and properties 3
                    # are ids found which satisfy conditions
                    # since they are a single tuples ,id_tuple[0] is id and here I make a list of properties ids
                    properties = [
                        id_tuple[0]
                        for id_tuple in list(
                            set(properties_1).intersection(set(properties_2)).intersection(set(properties_3))
                        )
                    ]
                # if properties 3 don't exist
                if properties_2:
                    properties = [id_tuple[0] for id_tuple in list(set(properties_1).intersection(set(properties_2)))]
                # if properties 2 don't exist
                if properties_3:
                    properties = [id_tuple[0] for id_tuple in list(set(properties_1).intersection(set(properties_3)))]
                    # if properties is made with properties 2 or 3
                if properties:
                    ad_repository = AdvertisementRepository(db)
                    return ad_repository.get_active_advertisements_by_property_id_and_type_of_ad_and_price(
                        min_price=min_price, max_price=max_price, type_of_ad=type_of_ad, properties_ids_list=properties
                    )
                # if properties 2 and 3 don't exist
                properties = [id_tuple[0] for id_tuple in properties_1]
                if properties:
                    ad_repository = AdvertisementRepository(db)
                    return ad_repository.get_active_advertisements_by_property_id_and_type_of_ad_and_price(
                        min_price=min_price, max_price=max_price, type_of_ad=type_of_ad, properties_ids_list=properties
                    )
                raise AdNotFoundByFilteredParametersException
        except Exception as exc:
            raise exc

    @staticmethod
    def update_status(clients_id: str, advertisement_id: str, status: str) -> Advertisement:
        """
        It updates the status of an advertisement if the client id of the
        advertisement is the same as the client id passed in the function
        """
        try:
            with SessionLocal() as db:
                ad_repo = AdvertisementRepository(db)
                clients_id_tuple = ad_repo.get_clients_id_by_advertisement_id(advertisement_id=advertisement_id)
                if clients_id_tuple[0] == clients_id:
                    return ad_repo.update_ad_status(advertisement_id=advertisement_id, status=status)
                raise NotAuthorizedException
        except Exception as exc:
            raise exc

    @staticmethod
    def update_ad_status_to_expired() -> list:
        """
        It updates the status of all ads that have expired to "expired"
        """
        try:
            with SessionLocal() as db:
                ad_repo = AdvertisementRepository(db)
                return ad_repo.update_ad_status_to_expired()
        except Exception as exc:
            raise exc

    @staticmethod
    def update_pending_status(advertisement_id: str, status: str) -> Advertisement:
        """
        It updates the status of an advertisement in the database
        """
        try:
            with SessionLocal() as db:
                ad_repo = AdvertisementRepository(db)
                return ad_repo.update_pending_status(advertisement_id=advertisement_id, status=status)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_stats(type_of_ad: Any, status: Any, type_of_property_id: str, city: str, start_date: str, end_date: str):
        """
        It gets the stats of the ads based on the given parameters
        """
        type_of_ad = None if type_of_ad is None else type_of_ad.value
        try:
            start_date = None if start_date is None else datetime.strptime(start_date, "%Y-%m-%d")
            end_date = None if end_date is None else datetime.strptime(end_date, "%Y-%m-%d")
        except Exception:
            raise EnterValidDateFormatException
        try:
            with SessionLocal() as db:
                if type_of_property_id:
                    TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
                ad_repository = AdvertisementRepository(db)
                # result is a tuple of 3 elements
                result = ad_repository.get_stats(
                    type_of_ad=type_of_ad,
                    status=status.value,
                    type_of_property_id=type_of_property_id,
                    city=city,
                    start_date=start_date,
                    end_date=end_date,
                )
                return {
                    "type_of_ad": type_of_ad,
                    "number_of_ads": result[0],
                    "status of ad": status.value,
                    "type_of_property_id": type_of_property_id,
                    "city": city,
                    "average_price_of_property": result[1],
                    "average_square_meter_price": result[2],
                }
        except Exception as exc:
            raise exc

    @staticmethod
    def get_stat_on_avg_price_by_city(
        type_of_ad: Any, status: Any, type_of_property_id: str, start_date: str, end_date: str
    ) -> dict:
        """
        It gets the stats on average price of square meter for city by search parameters
        """
        type_of_ad = None if type_of_ad is None else type_of_ad.value
        try:
            start_date = None if start_date is None else datetime.strptime(start_date, "%Y-%m-%d")
            end_date = None if end_date is None else datetime.strptime(end_date, "%Y-%m-%d")
        except Exception:
            raise EnterValidDateFormatException
        try:
            with SessionLocal() as db:
                if type_of_property_id:
                    TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
                ad_repository = AdvertisementRepository(db)
                ads_list = ad_repository.get_by_parameters_for_search(
                    type_of_ad=type_of_ad,
                    status=status.value,
                    type_of_property_id=type_of_property_id,
                    start_date=start_date,
                    end_date=end_date,
                )
                city_stats = {}
                for ad in ads_list:
                    if ad.property.city in city_stats:
                        city_stats[ad.property.city][0] += ad.price
                        city_stats[ad.property.city][1] += ad.property.square_meters
                    else:
                        city_stats.setdefault(ad.property.city, [ad.price, ad.property.square_meters])
                for city, (total_price, total_sqm) in city_stats.items():
                    city_stats[city] = total_price / total_sqm
                return city_stats
        except Exception as exc:
            raise exc
