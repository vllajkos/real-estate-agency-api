from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.advertisements.models import MoreLessEqual
from app.properties.exceptions import TypeOfPropertyDoesntSupportFeatureException, \
    PropertyDoesntHaveRequestedFeatureException
from app.properties.models import TypeOfPropertyHasFeature, TypeOfFeature
from app.properties.models import PropertyHasFeature


class PropertyHasFeatureRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, property_id: str, feature_id: str, additional_feature_value: int):
        try:
            property_feature = PropertyHasFeature(property_id=property_id, feature_id=feature_id,
                                                  additional_feature_value=additional_feature_value)
            self.db.add(property_feature)
            self.db.commit()
            self.db.refresh(property_feature)
            return property_feature
        except IntegrityError as err:
            raise err

    def get_property_with_feature_by_ids(self, property_id: str, feature_id: str):
        return self.db.query(PropertyHasFeature).filter((PropertyHasFeature.property_id == property_id) &
                                                        (PropertyHasFeature.feature_id == feature_id)).first()

    def get_all_features_for_property_by_id(self, property_id: str):
        return self.db.query(PropertyHasFeature).filter(PropertyHasFeature.property_id == property_id).all()

    def get_properties_ids_by_filter_parameters(self, features_id_list: list[str]) -> list:
        # returns filtered property's ids by filter parameters as single element tuple list
        return self.db.query(PropertyHasFeature.property_id).filter(
            PropertyHasFeature.feature_id.in_(features_id_list)).all()

    def get_properties_ids_by_feature_value(self, features_id_operator_value_list: list[tuple[str, str, int]]) -> list:
        # returns filtered property's ids by filter parameters as single element tuple list
        properties_ids_dict = {}
        property_ids_list = []
        # for feature operator value in list
        for feature_id, operator, value in features_id_operator_value_list:
            # if operator is > returns list of all property ids who fills the requirements
            if operator == MoreLessEqual.MORE.value:
                property_ids_list = self.db.query(PropertyHasFeature.property_id).filter(
                    (PropertyHasFeature.feature_id == feature_id) &
                    (PropertyHasFeature.additional_feature_value > value)).all()
            # if operator is < returns list of all property ids who fills the requirements
            elif operator == MoreLessEqual.LESS.value:
                property_ids_list = self.db.query(PropertyHasFeature.property_id).filter(
                    (PropertyHasFeature.feature_id == feature_id) &
                    (PropertyHasFeature.additional_feature_value < value)).all()
            # if operator is = returns list of all property ids who fills the requirements
            elif operator == MoreLessEqual.EQUAL.value:
                property_ids_list = self.db.query(PropertyHasFeature.property_id).filter(
                    (PropertyHasFeature.feature_id == feature_id) &
                    (PropertyHasFeature.additional_feature_value == value)).all()
            # if this is first pass property dict is empty
            if not properties_ids_dict:
                # property ids list is a list of tuples like ( id,) so I take first element
                for property_id in property_ids_list:
                    properties_ids_dict.setdefault(property_id[0], 1)
            else:
                # property ids list is a list of tuples like ( id,) so I take first element
                for property_id in property_ids_list:
                    # every pass for id value is +1 if satisfy conditions
                    if property_id[0] in properties_ids_dict:
                        properties_ids_dict[property_id[0]] += 1
            # if every time condition has been satisfied dict[id] should be same as len of feature list
            # otherwise some condition wasn't satisfied
            # returns a list of tuple of all property ids who meet conditions
        return [(property_id,) for property_id, value in properties_ids_dict.items()
                if properties_ids_dict[property_id] == len(features_id_operator_value_list)]

    def delete_feature_from_property_by_ids(self, property_id: str, feature_id: str):
        try:
            property_has_feature = self.get_property_with_feature_by_ids(property_id=property_id, feature_id=feature_id)
            if property_has_feature:
                self.db.delete(property_has_feature)
                self.db.commit()
                return
            raise PropertyDoesntHaveRequestedFeatureException
        except Exception as exc:
            raise exc
