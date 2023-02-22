"""Type of feature controller layer"""
from fastapi import HTTPException
from starlette.responses import JSONResponse
from app.properties.exceptions import TypeOfFeatureExistsException, TypeOfFeatureDoesntExistException, \
    TypeOfPropertyDoesntExistException, TypeOfPropertyDoesntHaveFeaturesException, CustomPropertyException
from app.properties.models import TypeOfFeature
from app.properties.services import TypeOfFeatureService


class TypeOfFeatureController:
    """Class containing Type of feature controller methods"""
    @staticmethod
    def create(feature: str, optional_values: bool) -> TypeOfFeature:
        """
        It creates a new type of feature
        """
        try:
            return TypeOfFeatureService.create(feature=feature, optional_values=optional_values)
        except TypeOfFeatureExistsException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all() -> list:
        """
        It returns all the TypeOfFeature objects in the database
        """
        try:
            return TypeOfFeatureService.get_all()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_by_feature(feature: str) -> TypeOfFeature:
        """
        It returns the type of feature by the feature name
        """
        try:
            return TypeOfFeatureService.get_by_feature(feature=feature)
        except TypeOfFeatureDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def get_by_id(feature_id: str) -> TypeOfFeature:
        """
        It gets the type of feature by id.
        """
        try:
            return TypeOfFeatureService.get_by_id(feature_id=feature_id)
        except TypeOfFeatureDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def get_features_for_type_of_property(type_id: str) -> list:
        """
        It returns the features for a given type of property
        """
        try:
            return TypeOfFeatureService.get_features_for_type_of_property_id(type_of_property_id=type_id)
        except TypeOfPropertyDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except TypeOfPropertyDoesntHaveFeaturesException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def delete_by_id(feature_id: str) -> JSONResponse:
        """
        It deletes a type of feature by its id
        """
        try:
            TypeOfFeatureService.delete_by_id(feature_id=feature_id)
            return JSONResponse(status_code=200, content="Type of feature deleted")
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
