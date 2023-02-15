from app.db import SessionLocal
from app.properties.exceptions import TypeOfPropertyHasFeatureExistsException, TypeOfPropertyDoesntExistException, \
    TypeOfFeatureDoesntExistException, TypeOfPropertyDoesntHaveFeaturesException, \
    TypeOfPropertyDoesntHaveFeatureException
from app.properties.repositories import TypeOfPropertyHasFeatureRepository, TypeOfPropertyRepository, \
    TypeOfFeatureRepository


class TypeOfPropertyHasFeatureService:

    @staticmethod
    def create(type_of_property_id: str, feature_id: str):
        try:
            with SessionLocal() as db:
                property_repo = TypeOfPropertyRepository(db)
                if not property_repo.get_by_id(type_id=type_of_property_id):
                    raise TypeOfPropertyDoesntExistException
                feature_repo = TypeOfFeatureRepository(db)
                if not feature_repo.get_by_id(feature_id=feature_id):
                    raise TypeOfFeatureDoesntExistException
                property_feature_repo = TypeOfPropertyHasFeatureRepository(db)
                if not property_feature_repo.get_property_with_feature_by_ids(type_of_property_id=type_of_property_id,
                                                                              feature_id=feature_id):
                    return property_feature_repo.create(type_of_property_id=type_of_property_id,
                                                        feature_id=feature_id)
                raise TypeOfPropertyHasFeatureExistsException
        except Exception as exc:
            raise exc

    @staticmethod
    def get_type_of_property_with_features(type_of_property_id: str):
        with SessionLocal() as db:
            property_repo = TypeOfPropertyRepository(db)
            if not property_repo.get_by_id(type_id=type_of_property_id):
                raise TypeOfPropertyDoesntExistException
            property_feature_repo = TypeOfPropertyHasFeatureRepository(db)
            features = property_feature_repo.get_type_of_property_with_features(type_of_property_id=type_of_property_id)
            if features:
                return features
            raise TypeOfPropertyDoesntHaveFeaturesException

    @staticmethod
    def delete(type_of_property_id: str, feature_id: str):
        try:
            with SessionLocal() as db:
                property_repo = TypeOfPropertyRepository(db)
                if not property_repo.get_by_id(type_id=type_of_property_id):
                    raise TypeOfPropertyDoesntExistException
                feature_repo = TypeOfFeatureRepository(db)
                if not feature_repo.get_by_id(feature_id=feature_id):
                    raise TypeOfFeatureDoesntExistException
                property_feature_repo = TypeOfPropertyHasFeatureRepository(db)
                if property_feature_repo.get_property_with_feature_by_ids(type_of_property_id=type_of_property_id,
                                                                          feature_id=feature_id):
                    return property_feature_repo.delete(type_of_property_id=type_of_property_id, feature_id=feature_id)
                raise TypeOfPropertyDoesntHaveFeatureException
        except Exception as exc:
            raise exc
