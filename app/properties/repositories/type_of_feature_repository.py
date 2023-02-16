"""Repository layer for types of features"""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.properties.exceptions import TypeOfFeatureDoesntExistException
from app.properties.models import TypeOfFeature, TypeOfPropertyHasFeature


class TypeOfFeatureRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, feature: str, optional_values: bool):
        try:
            feature_obj = TypeOfFeature(feature=feature, optional_values=optional_values)
            self.db.add(feature_obj)
            self.db.commit()
            self.db.refresh(feature_obj)
            return feature_obj
        except IntegrityError as err:
            raise err

    def get_optional_value_by_feature_id(self, feature_id: str):
        return self.db.query(TypeOfFeature.optional_values).filter(TypeOfFeature.id == feature_id).first()


    def get_by_feature(self, feature: str):
        return self.db.query(TypeOfFeature).filter(TypeOfFeature.feature == feature).first()

    def get_all(self):
        return self.db.query(TypeOfFeature).all()

    def get_by_id(self, feature_id: str):
        return self.db.query(TypeOfFeature).filter(TypeOfFeature.id == feature_id).first()

    def get_features_for_type_of_property_id(self, type_of_property_id: str):
        return self.db.query(TypeOfFeature).join(TypeOfPropertyHasFeature).filter(
            TypeOfPropertyHasFeature.type_of_property_id == type_of_property_id).all()

    def delete_by_id(self, feature_id: str):
        try:
            feature = self.db.query(TypeOfFeature).filter(TypeOfFeature.id == feature_id).first()
            if feature is None:
                raise TypeOfFeatureDoesntExistException
            self.db.delete(feature)
            self.db.commit()
            return True
        except Exception as exc:
            raise exc
