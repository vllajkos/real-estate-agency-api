from typing import Any

from fastapi import HTTPException

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
    def get_all_active_ads():
        try:
            return AdvertisementService.get_all_active_ads()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_active_ads_by_type_of_ad(type_of_ad: Any):
        try:
            return AdvertisementService.get_all_active_ads_by_type_of_ad(type_of_ad=type_of_ad)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_active_ads_by_type_of_ad_and_type_of_property_id(type_of_ad: Any, type_of_property_id: str):
        try:
            return AdvertisementService.get_all_active_ads_by_type_of_ad_and_type_of_property_id(
                type_of_ad=type_of_ad, type_of_property_id=type_of_property_id)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

