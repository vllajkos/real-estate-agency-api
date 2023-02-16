from fastapi import HTTPException
from starlette.responses import JSONResponse

from app.properties.exceptions import CustomPropertyException

from app.properties.services import PropertyHasFeatureService


class PropertyHasFeatureController:

    @staticmethod
    def create(property_id: str, feature_id: str, additional_feature_value: int):
        try:
            return PropertyHasFeatureService.create(property_id=property_id, feature_id=feature_id,
                                                    additional_feature_value=additional_feature_value)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_features_for_property_by_id(property_id: str):
        try:
            return PropertyHasFeatureService.get_all_features_for_property_by_id(property_id=property_id)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def delete_feature_from_property_by_ids(property_id: str, feature_id: str):
        try:
            PropertyHasFeatureService.delete_feature_from_property_by_ids(property_id=property_id,
                                                                          feature_id=feature_id)
            return JSONResponse(status_code=200, content=f"Feature deleted for property id {property_id}")
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
