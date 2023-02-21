from fastapi import HTTPException
from starlette.responses import JSONResponse

from app.properties.exceptions import CustomPropertyException
from app.properties.services.type_of_property_has_feature_services import TypeOfPropertyHasFeatureService


class TypeOfPropertyHasFeatureController:

    @staticmethod
    def create(type_of_property_id: str, feature_id: str):
        try:
            return TypeOfPropertyHasFeatureService.create(type_of_property_id=type_of_property_id,
                                                          feature_id=feature_id)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_type_of_property_with_features(type_id: str):
        try:
            return TypeOfPropertyHasFeatureService.get_type_of_property_with_features(type_of_property_id=type_id)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def get_type_of_property_with_features_by_optional_values(type_id: str, optional_values: bool):
        try:
            return TypeOfPropertyHasFeatureService.get_type_of_property_with_features_by_optional_values(
                type_of_property_id=type_id, optional_values=optional_values)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    # @staticmethod
    # def get_features_for_type_of_property(type_id: str):
    #     try:
    #         return TypeOfPropertyHasFeatureService.get_features_for_type_of_property_id(type_of_property_id=type_id)
    #     except TypeOfPropertyDoesntExistException as exc:
    #         raise HTTPException(status_code=exc.status_code, detail=exc.message)
    #     except TypeOfPropertyDoesntHaveFeaturesException as exc:
    #         raise HTTPException(status_code=exc.status_code, detail=exc.message)
    @staticmethod
    def delete(type_id: str, feature_id: str):
        try:
            TypeOfPropertyHasFeatureService.delete(type_of_property_id=type_id, feature_id=feature_id)
            return JSONResponse(status_code=200, content=f"Feature with id {feature_id} removed "
                                                         f"from type of property id {type_id}")
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    # @staticmethod
    # def get_nesto(type_id: str):
    #     return TypeOfPropertyHasFeatureService.get_nesto(type=type_id)
