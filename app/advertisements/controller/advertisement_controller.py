from typing import Any

from fastapi import HTTPException
from starlette.responses import JSONResponse

from app.advertisements.exceptions import CustomAdvertisementExceptions
from app.advertisements.services import AdvertisementService
from app.properties.exceptions.property_exceptions import CustomPropertyException
from app.users.exceptions.custom_user_exception import CustomUserException


class AdvertisementController:

    @staticmethod
    def create(type_of_ad: Any, price: float, description: str, property_id: str, client_id: str):
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
    def get_all_on_pending_for_employee_id(employee_id: str):
        try:
            return AdvertisementService.get_all_on_pending_for_employee_id(employee_id=employee_id)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_active_advertisement_by_id(advertisement_id: str):
        try:
            return AdvertisementService.get_active_advertisement_by_id(advertisement_id=advertisement_id)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_active_ads():
        try:
            return AdvertisementService.get_all_active_ads()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_active_ads_by_type_of_ad_sorted(type_of_ad: Any, sort_: Any):
        try:
            return AdvertisementService.get_all_active_ads_by_type_of_ad_sorted(type_of_ad=type_of_ad, sort_=sort_)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_active_ads_by_type_of_ad_and_type_of_property_id(type_of_ad: Any, type_of_property_id: str):
        try:
            return AdvertisementService.get_all_active_ads_by_type_of_ad_and_type_of_property_id(
                type_of_ad=type_of_ad, type_of_property_id=type_of_property_id)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_by_ad_and_property_types_and_city(type_of_ad: Any, type_of_property_id: str, city: str):
        try:
            return AdvertisementService.get_all_by_ad_and_property_types_and_city(
                type_of_ad=type_of_ad, type_of_property_id=type_of_property_id, city=city)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_by_filter_parameters(type_of_ad: str, min_price: float, max_price: float,
                                 municipality: str, city: str, country: str, min_square_meters: float,
                                 max_square_meters: float, type_of_property_id: str, feature_id_list: list[str],
                                 features_id_operator_value_list: list[tuple[str, str, int]]):
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
    def update_ad_status(clients_id: str, advertisement_id: str, status: Any):
        try:
            return AdvertisementService.update_status(clients_id=clients_id,
                                                      advertisement_id=advertisement_id, status=status)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def update_ad_status_to_expired():
        try:
            return AdvertisementService.update_ad_status_to_expired()
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def update_pending_status(advertisement_id: str, status: Any):
        try:
            return AdvertisementService.update_pending_status(advertisement_id=advertisement_id, status=status)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_stats(type_of_ad: Any, type_of_property_id: str, city: str, start_date: str, end_date: str):
        try:
            content = AdvertisementService.get_stats(type_of_ad=type_of_ad, type_of_property_id=type_of_property_id,
                                                     city=city, start_date=start_date, end_date=end_date)
            return JSONResponse(content=content)
        except CustomAdvertisementExceptions as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
