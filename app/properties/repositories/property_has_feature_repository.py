from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

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



    # def get_property_with_feature_by_ids(self, type_of_property_id: str, feature_id: str):
    #     return self.db.query(TypeOfPropertyHasFeature).filter(
    #         (TypeOfPropertyHasFeature.type_of_property_id == type_of_property_id) &
    #         (TypeOfPropertyHasFeature.feature_id == feature_id)).first()
    #
    # # def get_features_for_type_of_property_id(self, type_of_property_id: str):
    # #     return self.db.query(TypeOfFeature).join(TypeOfPropertyHasFeature).filter(
    # #         TypeOfPropertyHasFeature.type_of_property_id == type_of_property_id).all()
    #
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
