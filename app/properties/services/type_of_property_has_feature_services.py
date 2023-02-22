""" Service layer for types of properties have types of features"""
from app.db import SessionLocal
from app.properties.exceptions import TypeOfPropertyHasFeatureExistsException, \
    TypeOfPropertyDoesntHaveFeaturesException, TypeOfPropertyDoesntSupportFeatureException
from app.properties.models import TypeOfPropertyHasFeature
from app.properties.repositories import TypeOfPropertyHasFeatureRepository
from app.properties.services import TypeOfPropertyService, TypeOfFeatureService


class TypeOfPropertyHasFeatureService:
    """Class containing methods of a service layer of types of properties have types of features"""

    @staticmethod
    def create(type_of_property_id: str, feature_id: str) -> TypeOfPropertyHasFeature:
        """
        It creates a new type of property has feature relationship if it doesn't exist
        """
        try:
            with SessionLocal() as db:
                TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
                TypeOfFeatureService.get_by_id(feature_id=feature_id)
                property_feature_repo = TypeOfPropertyHasFeatureRepository(db)

                if not property_feature_repo.get_type_of_property_and_type_of_feature_by_ids(
                        type_of_property_id=type_of_property_id, feature_id=feature_id):
                    return property_feature_repo.create(type_of_property_id=type_of_property_id,
                                                        feature_id=feature_id)
                raise TypeOfPropertyHasFeatureExistsException
        except Exception as exc:
            raise exc

    @staticmethod
    def get_type_of_property_with_features(type_of_property_id: str) -> list:
        """
        It gets the type of property by id and then gets the features of that type of property
        """
        with SessionLocal() as db:
            TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
            property_feature_repo = TypeOfPropertyHasFeatureRepository(db)
            features = property_feature_repo.get_type_of_property_with_features(type_of_property_id=type_of_property_id)
            if features:
                return features
            raise TypeOfPropertyDoesntHaveFeaturesException

    @staticmethod
    def get_type_of_property_with_features_by_optional_values(type_of_property_id: str, optional_values: bool) -> list:
        """
        It gets the type of property by id and then gets the features of that type of property by optional values
        """
        with SessionLocal() as db:
            TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
            property_feature_repo = TypeOfPropertyHasFeatureRepository(db)
            features = property_feature_repo.get_type_of_property_with_features_by_optional_values(
                type_of_property_id=type_of_property_id, optional_values=optional_values)
            if features:
                return features
            raise TypeOfPropertyDoesntHaveFeaturesException

    @staticmethod
    def get_type_of_property_and_type_of_feature_by_ids(type_of_property_id: str,
                                                        feature_id: str) -> TypeOfPropertyHasFeature:
        """
        It gets a type of property and a feature by their ids
        """
        with SessionLocal() as db:
            property_feature_repo = TypeOfPropertyHasFeatureRepository(db)
            property_feature = property_feature_repo.get_type_of_property_and_type_of_feature_by_ids(
                type_of_property_id=type_of_property_id, feature_id=feature_id)
            if property_feature:
                return property_feature
            raise TypeOfPropertyDoesntSupportFeatureException

    @staticmethod
    def delete(type_of_property_id: str, feature_id: str) -> bool:
        """
        It deletes a relationship between a type of property and a type of feature
        """
        try:
            with SessionLocal() as db:
                TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
                TypeOfFeatureService.get_by_id(feature_id=feature_id)
                property_feature_repo = TypeOfPropertyHasFeatureRepository(db)
                if property_feature_repo.get_type_of_property_and_type_of_feature_by_ids(
                        type_of_property_id=type_of_property_id, feature_id=feature_id):
                    return property_feature_repo.delete(type_of_property_id=type_of_property_id, feature_id=feature_id)
                raise TypeOfPropertyDoesntSupportFeatureException
        except Exception as exc:
            raise exc
