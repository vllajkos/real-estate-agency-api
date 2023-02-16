from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.properties.exceptions import TypeOfPropertyDoesntSupportFeatureException
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
    #
    # def get_type_of_property_with_features(self, type_of_property_id: str):
    #     return self.db.query(TypeOfPropertyHasFeature).filter(
    #         TypeOfPropertyHasFeature.type_of_property_id == type_of_property_id).all()
    #
    # def get_property_with_feature_by_ids(self, type_of_property_id: str, feature_id: str):
    #     return self.db.query(TypeOfPropertyHasFeature).filter(
    #         (TypeOfPropertyHasFeature.type_of_property_id == type_of_property_id) &
    #         (TypeOfPropertyHasFeature.feature_id == feature_id)).first()
    #
    # # def get_features_for_type_of_property_id(self, type_of_property_id: str):
    # #     return self.db.query(TypeOfFeature).join(TypeOfPropertyHasFeature).filter(
    # #         TypeOfPropertyHasFeature.type_of_property_id == type_of_property_id).all()
    #
    # def delete(self, type_of_property_id: str, feature_id: str):
    #     try:
    #         property_with_feature = self.get_property_with_feature_by_ids(type_of_property_id=type_of_property_id,
    #                                                                       feature_id=feature_id)
    #         if property_with_feature:
    #             self.db.delete(property_with_feature)
    #             self.db.commit()
    #             return True
    #         raise TypeOfPropertyDoesntHaveFeatureException
    #     except Exception as exc:
    #         raise exc
