"""Type of feature service layer"""

from app.db import SessionLocal
from app.properties.exceptions import (
    TypeOfFeatureDoesntExistException,
    TypeOfFeatureExistsException,
    TypeOfPropertyDoesntHaveFeaturesException,
)
from app.properties.models import TypeOfFeature
from app.properties.repositories import TypeOfFeatureRepository
from app.properties.services import TypeOfPropertyService


class TypeOfFeatureService:
    """Class containing methods of a service layer for types of features"""

    @staticmethod
    def create(feature: str, optional_values: bool) -> TypeOfFeature:
        """
        It creates a new type of feature in the database
        """
        try:
            with SessionLocal() as db:
                feature_repository = TypeOfFeatureRepository(db=db)
                if feature_repository.get_by_feature(feature=feature):
                    raise TypeOfFeatureExistsException
                return feature_repository.create(feature=feature, optional_values=optional_values)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_optional_value_by_feature_id(feature_id: str) -> tuple | None:
        """
        It gets the optional value of a feature by its id
        """
        try:
            with SessionLocal() as db:
                feature_repository = TypeOfFeatureRepository(db=db)
                feature_obj = feature_repository.get_by_id(feature_id=feature_id)
                if feature_obj is None:
                    raise TypeOfFeatureDoesntExistException
                return feature_repository.get_optional_value_by_feature_id(feature_id=feature_id)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all() -> list:
        """
        It gets all the features from the database
        """
        try:
            with SessionLocal() as db:
                feature_repository = TypeOfFeatureRepository(db=db)
                return feature_repository.get_all()
        except Exception as exc:
            raise exc

    @staticmethod
    def get_by_feature(feature: str) -> TypeOfFeature:
        """
        It gets a feature object from the database by its feature name
        """
        with SessionLocal() as db:
            feature_repository = TypeOfFeatureRepository(db=db)
            feature_obj = feature_repository.get_by_feature(feature=feature)
            if feature_obj is None:
                raise TypeOfFeatureDoesntExistException
            return feature_obj

    @staticmethod
    def get_by_id(feature_id: str) -> TypeOfFeature:
        """
        It gets a feature by its id
        """
        with SessionLocal() as db:
            feature_repository = TypeOfFeatureRepository(db=db)
            feature_obj = feature_repository.get_by_id(feature_id=feature_id)
            if feature_obj is None:
                raise TypeOfFeatureDoesntExistException
            return feature_obj

    @staticmethod
    def get_features_for_type_of_property_id(type_of_property_id: str) -> list:
        """
        It gets the features for a type of property id
        """
        with SessionLocal() as db:
            TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
            feature_repo = TypeOfFeatureRepository(db)
            features_list = feature_repo.get_features_for_type_of_property_id(type_of_property_id=type_of_property_id)
            if features_list:
                return features_list
            raise TypeOfPropertyDoesntHaveFeaturesException

    @staticmethod
    def delete_by_id(feature_id: str) -> None:
        """
        It deletes a feature by its id
        """
        try:
            with SessionLocal() as db:
                feature_repository = TypeOfFeatureRepository(db=db)
                feature_repository.delete_by_id(feature_id=feature_id)
        except Exception as exc:
            raise exc
