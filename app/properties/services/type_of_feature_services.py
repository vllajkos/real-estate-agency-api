from app.db import SessionLocal
from app.properties.exceptions import TypeOfFeatureExistsException, TypeOfFeatureDoesntExistException, \
    TypeOfPropertyDoesntHaveFeaturesException
from app.properties.repositories import TypeOfFeatureRepository, TypeOfPropertyHasFeatureRepository
from app.properties.services import TypeOfPropertyService


class TypeOfFeatureService:

    @staticmethod
    def create(feature: str, optional_values: bool):
        try:
            with SessionLocal() as db:
                feature_repository = TypeOfFeatureRepository(db=db)
                if feature_repository.get_by_feature(feature=feature):
                    raise TypeOfFeatureExistsException
                return feature_repository.create(feature=feature, optional_values=optional_values)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_optional_value_by_feature_id(feature_id: str):
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
    def get_all():
        try:
            with SessionLocal() as db:
                feature_repository = TypeOfFeatureRepository(db=db)
                return feature_repository.get_all()
        except Exception as exc:
            raise exc

    @staticmethod
    def get_by_feature(feature: str):
        with SessionLocal() as db:
            feature_repository = TypeOfFeatureRepository(db=db)
            feature_obj = feature_repository.get_by_feature(feature=feature)
            if feature_obj is None:
                raise TypeOfFeatureDoesntExistException
            return feature_obj

    @staticmethod
    def get_by_id(feature_id: str):
        with SessionLocal() as db:
            feature_repository = TypeOfFeatureRepository(db=db)
            feature_obj = feature_repository.get_by_id(feature_id=feature_id)
            if feature_obj is None:
                raise TypeOfFeatureDoesntExistException
            return feature_obj

    @staticmethod
    def get_features_for_type_of_property_id(type_of_property_id: str):
        with SessionLocal() as db:
            TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
            feature_repo = TypeOfFeatureRepository(db)
            features_list = feature_repo.get_features_for_type_of_property_id(type_of_property_id=type_of_property_id)
            if features_list:
                return features_list
            raise TypeOfPropertyDoesntHaveFeaturesException


    @staticmethod
    def delete_by_id(feature_id: str):
        try:
            with SessionLocal() as db:
                feature_repository = TypeOfFeatureRepository(db=db)
                feature_repository.delete_by_id(feature_id=feature_id)
        except Exception as exc:
            raise exc
