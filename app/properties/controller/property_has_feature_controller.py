"""Property has feature controller layer"""
from fastapi import HTTPException
from starlette.responses import JSONResponse
from app.properties.exceptions import CustomPropertyException
from app.properties.models import PropertyHasFeature
from app.properties.services import PropertyHasFeatureService


class PropertyHasFeatureController:
    """Class containing Property has feature controller methods"""
    @staticmethod
    def create(property_id: str, feature_id: str, additional_feature_value: int = None) -> PropertyHasFeature:
        """
        Creates bond between existing property and chosen features for that property
        """
        try:
            return PropertyHasFeatureService.create(property_id=property_id, feature_id=feature_id,
                                                    additional_feature_value=additional_feature_value)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_features_for_property_by_id(property_id: str) -> list:
        """
        Gets all features for property by id
        """
        try:
            return PropertyHasFeatureService.get_all_features_for_property_by_id(property_id=property_id)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def delete_feature_from_property_by_ids(property_id: str, feature_id: str) -> JSONResponse:
        """
         Delete a feature from a property by property id and feature id
        """
        try:
            PropertyHasFeatureService.delete_feature_from_property_by_ids(property_id=property_id,
                                                                          feature_id=feature_id)
            return JSONResponse(status_code=200, content=f"Feature deleted for property id {property_id}")
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
