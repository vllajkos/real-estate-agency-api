"""Property has feature service layer"""
from app.advertisements.models import MoreLessEqual
from app.db import SessionLocal
from app.properties.exceptions import PropertyAlreadyHasThatFeatureException, \
    TypeOfFeatureDoesntSupportAdditionalValueException, PropertyDoesntHaveFeaturesException, \
    PropertyDoesntHaveRequestedFeatureException, PropertiesNotFoundByFilterParametersException
from app.properties.models import PropertyHasFeature
from app.properties.repositories import PropertyHasFeatureRepository
from app.properties.services import TypeOfFeatureService, PropertyService
from app.properties.services import TypeOfPropertyHasFeatureService as CheckFeatureSupport


class PropertyHasFeatureService:
    """Class containing method Property has feature service layer"""

    @staticmethod
    def create(property_id: str, feature_id: str, additional_feature_value: int) -> PropertyHasFeature:
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
    def get_all_features_for_property_by_id(property_id: str) -> list:
        """
        It gets all the features for a property by its id
        """
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
    def get_properties_ids_by_filter_parameters(features_id_list: list[str]) -> list:
        """
        It returns a list of ids of properties having needed features
        """
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
    def get_properties_ids_by_feature_value(features_id_operator_value_list: list[tuple[str, str, int]]) -> list:
        """
        It takes a list of tuples of feature id, operator and value,
         and returns a list of tuples of property ids that have
        at least one of those features and pass the operator check
        """
        # this is used in advertisement search only
        # returns a list of ids of properties having needed features
        try:
            with SessionLocal() as db:
                # making a list of features ids from list of tuples
                feature_id_list = [tuple_feature[0] for tuple_feature in features_id_operator_value_list]
                property_feature_repo = PropertyHasFeatureRepository(db)
                # giving that list to repository to return properties that contain at least one of those features
                # by checking if property has at least one feature from that list
                property_has_feature_list = property_feature_repo.get_properties_by_features_list(
                    features_id_list=feature_id_list)
                properties_id_dict = {}
                # unpacking tuples from feature_id_operator_value_list
                for filter_feature_id, operator, filter_value in features_id_operator_value_list:
                    # for every object of PropertyHasFeature type in list returned from first filter
                    for property_has_feature_object in property_has_feature_list:
                        # if needed feature id from request is equal to PropertyHasFeature object's feature id
                        if filter_feature_id == property_has_feature_object.feature_id:
                            # # checking which operator is being given for that feature id
                            if operator == MoreLessEqual.LESS.value:
                                # compare given value with object's value with that operator
                                if filter_value > property_has_feature_object.additional_feature_value:
                                    # if passes an operator check, checks if that property id is in properties ids dict
                                    # if exists as a key value is raised for 1 more pass
                                    if property_has_feature_object.property_id in properties_id_dict:
                                        properties_id_dict[property_has_feature_object.property_id] += 1
                                    # if not it sets key to property id and value to 1
                                    else:
                                        properties_id_dict.setdefault(property_has_feature_object.property_id, 1)
                            # same logic goes for other to operators
                            elif operator == MoreLessEqual.MORE.value:
                                if filter_value < property_has_feature_object.additional_feature_value:
                                    if property_has_feature_object.property_id in properties_id_dict:
                                        properties_id_dict[property_has_feature_object.property_id] += 1
                                    else:
                                        properties_id_dict.setdefault(property_has_feature_object.property_id, 1)
                            elif operator == MoreLessEqual.EQUAL.value:
                                if filter_value == property_has_feature_object.additional_feature_value:
                                    if property_has_feature_object.property_id in properties_id_dict:
                                        properties_id_dict[property_has_feature_object.property_id] += 1
                                    else:
                                        properties_id_dict.setdefault(property_has_feature_object.property_id, 1)
                # finally creates a list of properties ids as a list of single element tuple for those
                # property ids that have passed all searching parameters by comparing value which represents
                # number of passed filters vs number of provided filters
                # if it is the same as  number than property id is added to the list
                properties_ids_list = [(property_id,) for property_id, value in properties_id_dict.items()
                                       if properties_id_dict[property_has_feature_object.property_id] == len(
                        features_id_operator_value_list)]
                # if not empty returns list else raises an exception
                if properties_ids_list:
                    return properties_ids_list
                raise PropertiesNotFoundByFilterParametersException
        except Exception as exc:
            raise exc

    @staticmethod
    def delete_feature_from_property_by_ids(property_id: str, feature_id: str) -> None:
        """
        It deletes a feature from a property by the property and feature ids
        """
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
