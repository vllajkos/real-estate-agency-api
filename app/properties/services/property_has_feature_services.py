from app.db import SessionLocal
from app.properties.exceptions import PropertyAlreadyHasThatFeatureException, \
    TypeOfFeatureDoesntSupportAdditionalValueException, PropertyDoesntHaveFeaturesException, \
    PropertyDoesntHaveRequestedFeatureException, PropertiesNotFoundByFilterParametersException
from app.properties.repositories import PropertyHasFeatureRepository
from app.properties.services import TypeOfFeatureService, PropertyService
from app.properties.services import TypeOfPropertyHasFeatureService as CheckFeatureSupport


class PropertyHasFeatureService:

    @staticmethod
    def create(property_id: str, feature_id: str, additional_feature_value: int):
        """ This method creates a bond between concrete property created by user and features available for that
        concrete type of property which user can add to his property if feature is supported by type of property """
        try:
            with SessionLocal() as db:
                # this checks if property_id exists in database
                property_ = PropertyService.get_property_by_id(property_id=property_id)
                # this returns a tuple from database providing info if feature have optional values (False,) or (True,)
                # if feature id doesn't exist raises an exception
                if not TypeOfFeatureService.get_optional_value_by_feature_id(feature_id=feature_id)[0]:
                    # need to check if feature is supported for type of property
                    CheckFeatureSupport.get_type_of_property_and_type_of_feature_by_ids(
                        type_of_property_id=property_.type_of_property_id, feature_id=feature_id)
                    # if additional value is given raises an exception
                    if additional_feature_value:
                        raise TypeOfFeatureDoesntSupportAdditionalValueException
                property_feature = PropertyHasFeatureRepository(db=db)
                if property_feature.get_property_with_feature_by_ids(property_id=property_id, feature_id=feature_id):
                    raise PropertyAlreadyHasThatFeatureException
                return property_feature.create(property_id=property_id, feature_id=feature_id,
                                               additional_feature_value=additional_feature_value)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_features_for_property_by_id(property_id: str):
        try:
            with SessionLocal() as db:
                PropertyService.get_property_by_id(property_id=property_id)
                property_feature_repo = PropertyHasFeatureRepository(db)
                features = property_feature_repo.get_all_features_for_property_by_id(property_id=property_id)
                if features:
                    return features
                raise PropertyDoesntHaveFeaturesException
        except Exception as exc:
            raise exc

    @staticmethod
    def get_properties_ids_by_filter_parameters(features_id_list: list[str]):
        # this is used in advertisement search only
        # returns a list of ids of properties having needed features
        try:
            with SessionLocal() as db:
                property_feature_repo = PropertyHasFeatureRepository(db)
                properties_ids = property_feature_repo.get_properties_ids_by_filter_parameters(
                    features_id_list=features_id_list)
                if properties_ids:
                    return properties_ids
                raise PropertiesNotFoundByFilterParametersException
        except Exception as exc:
            raise exc

    @staticmethod
    def delete_feature_from_property_by_ids(property_id: str, feature_id: str):
        try:
            with SessionLocal() as db:
                PropertyService.get_property_by_id(property_id=property_id)
                TypeOfFeatureService.get_by_id(feature_id=feature_id)
                property_feature_repo = PropertyHasFeatureRepository(db)
                if property_feature_repo.get_property_with_feature_by_ids(property_id=property_id,
                                                                          feature_id=feature_id):
                    return property_feature_repo.delete_feature_from_property_by_ids(property_id=property_id,
                                                                                     feature_id=feature_id)
                raise PropertyDoesntHaveRequestedFeatureException
        except Exception as exc:
            raise exc
