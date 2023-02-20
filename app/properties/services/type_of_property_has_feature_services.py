from app.db import SessionLocal
from app.properties.exceptions import TypeOfPropertyHasFeatureExistsException, TypeOfPropertyDoesntExistException, \
    TypeOfFeatureDoesntExistException, TypeOfPropertyDoesntHaveFeaturesException, \
    TypeOfPropertyDoesntSupportFeatureException
from app.properties.repositories import TypeOfPropertyHasFeatureRepository, TypeOfPropertyRepository, \
    TypeOfFeatureRepository
from app.properties.services import TypeOfPropertyService, TypeOfFeatureService


class TypeOfPropertyHasFeatureService:

    @staticmethod
    def create(type_of_property_id: str, feature_id: str):
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
    def get_type_of_property_with_features(type_of_property_id: str):
        with SessionLocal() as db:
            TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
            property_feature_repo = TypeOfPropertyHasFeatureRepository(db)
            features = property_feature_repo.get_type_of_property_with_features(type_of_property_id=type_of_property_id)
            if features:
                return features
            raise TypeOfPropertyDoesntHaveFeaturesException

    @staticmethod
    def get_type_of_property_with_features_by_optional_values(type_of_property_id: str, optional_values: bool):
        with SessionLocal() as db:
            TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
            property_feature_repo = TypeOfPropertyHasFeatureRepository(db)
            features = property_feature_repo.get_type_of_property_with_features_by_optional_values(
                type_of_property_id=type_of_property_id, optional_values=optional_values)
            if features:
                return features
            raise TypeOfPropertyDoesntHaveFeaturesException

    # @staticmethod
    # def get_features_for_type_of_property_id(type_of_property_id: str):
    #     with SessionLocal() as db:
    #         TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
    #         property_feature_repo = TypeOfPropertyHasFeatureRepository(db)
    #         pr_feat = property_feature_repo.get_type_of_property_with_features(type_of_property_id=type_of_property_id)
    #         if pr_feat:
    #             features_list = []
    #             for property_feature in pr_feat:
    #                 feature = TypeOfFeatureService.get_by_id(feature_id=property_feature.feature_id)
    #                 features_list.append(feature)
    #             return features_list
    #         raise TypeOfPropertyDoesntHaveFeaturesException

    @staticmethod
    def get_type_of_property_and_type_of_feature_by_ids(type_of_property_id: str, feature_id: str):
        with SessionLocal() as db:
            property_feature_repo = TypeOfPropertyHasFeatureRepository(db)
            property_feature = property_feature_repo.get_type_of_property_and_type_of_feature_by_ids(
                type_of_property_id=type_of_property_id, feature_id=feature_id)
            if property_feature:
                return property_feature
            raise TypeOfPropertyDoesntSupportFeatureException

    @staticmethod
    def delete(type_of_property_id: str, feature_id: str):
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
