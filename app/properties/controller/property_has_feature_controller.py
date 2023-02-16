from fastapi import HTTPException

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
