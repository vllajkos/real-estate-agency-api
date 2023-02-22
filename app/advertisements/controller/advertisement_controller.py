"""Controller layer for advertisement"""
from typing import Any
from fastapi import HTTPException
from starlette.responses import JSONResponse
from app.advertisements.exceptions import CustomAdvertisementExceptions
from app.advertisements.models import Advertisement
from app.advertisements.services import AdvertisementService
from app.properties.exceptions.property_exceptions import CustomPropertyException
from app.users.exceptions.custom_user_exception import CustomUserException


class AdvertisementController:
    """Class containing methods for controller layer of advertisement"""
    @staticmethod
    def create(type_of_ad: Any, price: float, description: str, property_id: str, client_id: str) -> Advertisement:
        """
        It creates an advertisement
        """
        try:
            return AdvertisementService.create(type_of_ad=type_of_ad, price=price, description=description,
                                               property_id=property_id, client_id=client_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_active_for_client_id(client_id: str) -> list:
        """
        It returns all active advertisements for a given client id
        """
        try:
            return AdvertisementService.get_all_active_for_client_id(client_id=client_id)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_on_pending_for_employee_id(employee_id: str) -> list:
        """
        Returns all advertisements that are on pending for a given employee id
        """
        try:
            return AdvertisementService.get_all_on_pending_for_employee_id(employee_id=employee_id)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
    @staticmethod
    def get_active_advertisement_by_id(advertisement_id: str) -> list:
        """
        Returns an active advertisement by id
        """
        try:
            return AdvertisementService.get_active_advertisement_by_id(advertisement_id=advertisement_id)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_active_ads() -> list:
        """
        It returns all active ads
        """
        try:
            return AdvertisementService.get_all_active_ads()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_active_ads_by_type_of_ad_sorted(type_of_ad: Any, sort_: Any) -> list:
        """
        Returns a list of all active ads of a given type of ad, sorted by a given
        sort type
        """
        try:
            return AdvertisementService.get_all_active_ads_by_type_of_ad_sorted(type_of_ad=type_of_ad, sort_=sort_)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_active_ads_by_type_of_ad_and_type_of_property_id(type_of_ad: Any, type_of_property_id: str) -> list:
        """
        Get all active ads by type of ad and type of property
        """
        try:
            return AdvertisementService.get_all_active_ads_by_type_of_ad_and_type_of_property_id(
                type_of_ad=type_of_ad, type_of_property_id=type_of_property_id)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_by_ad_and_property_types_and_city(type_of_ad: Any, type_of_property_id: str, city: str) -> list:
        """
        It returns all the advertisements that match the given type of ad, type of property and city
        """
        try:
            return AdvertisementService.get_all_by_ad_and_property_types_and_city(
                type_of_ad=type_of_ad, type_of_property_id=type_of_property_id, city=city)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_by_filter_parameters(type_of_ad: str, min_price: float, max_price: float,
                                 municipality: str, city: str, country: str, min_square_meters: float,
                                 max_square_meters: float, type_of_property_id: str, feature_id_list: list[str],
                                 features_id_operator_value_list: list[tuple[str, str, int]]) -> list:
        """ Get all active ads by filter parameters"""
        try:
            return AdvertisementService.get_by_filter_parameters(type_of_ad=type_of_ad,
                                                                 min_price=min_price,
                                                                 max_price=max_price,
                                                                 municipality=municipality,
                                                                 city=city, country=country,
                                                                 min_square_meters=min_square_meters,
                                                                 max_square_meters=max_square_meters,
                                                                 type_of_property_id=type_of_property_id,
                                                                 feature_id_list=feature_id_list,
                                                                 features_id_operator_value_list=
                                                                 features_id_operator_value_list)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def update_ad_status(clients_id: str, advertisement_id: str, status: Any) -> Advertisement:
        """
        It updates the status of an advertisement by user
        """
        try:
            return AdvertisementService.update_status(clients_id=clients_id,
                                                      advertisement_id=advertisement_id, status=status)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def update_ad_status_to_expired() -> list:
        """
        It updates the status of all the ads that have expired to 'expired'
        """
        try:
            return AdvertisementService.update_ad_status_to_expired()
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def update_pending_status(advertisement_id: str, status: Any) -> Advertisement:
        """
        It updates the pending status of an advertisement.
        """
        try:
            return AdvertisementService.update_pending_status(advertisement_id=advertisement_id, status=status)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_stats(type_of_ad: Any, status: Any, type_of_property_id: str, city: str, start_date: str,
                  end_date: str) -> JSONResponse:
        """
        It returns the stats of the advertisements based on the given parameters
        """
        try:
            content = AdvertisementService.get_stats(type_of_ad=type_of_ad, status=status,
                                                     type_of_property_id=type_of_property_id,
                                                     city=city, start_date=start_date, end_date=end_date)
            return JSONResponse(content=content)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
