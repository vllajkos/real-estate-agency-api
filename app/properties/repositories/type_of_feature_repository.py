"""Repository layer for types of features"""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.properties.exceptions import TypeOfFeatureDoesntExistException
from app.properties.models import TypeOfFeature, TypeOfPropertyHasFeature


class TypeOfFeatureRepository:
    """Repository layer containing crud methods for type of feature"""
    def __init__(self, db: Session) -> None:
        """ Model of repository object"""
        self.db = db

    def create(self, feature: str, optional_values: bool) -> TypeOfFeature:
        """
        It creates a new feature object and adds it to the database
        """
        try:
            feature_obj = TypeOfFeature(feature=feature, optional_values=optional_values)
            self.db.add(feature_obj)
            self.db.commit()
            self.db.refresh(feature_obj)
            return feature_obj
        except IntegrityError as err:
            raise err

    def get_optional_value_by_feature_id(self, feature_id: str) -> tuple | None:
        """
        It returns the optional values of a feature by its id
        """
        return self.db.query(TypeOfFeature.optional_values).filter(TypeOfFeature.id == feature_id).first()

    def get_by_feature(self, feature: str) -> TypeOfFeature | None:
        """
        It returns the first instance of the TypeOfFeature class where the feature attribute is equal to the feature
        parameter
        """
        return self.db.query(TypeOfFeature).filter(TypeOfFeature.feature == feature).first()

    def get_all(self) -> list:
        """
        It returns all the rows in the TypeOfFeature table
        """
        return self.db.query(TypeOfFeature).all()

    def get_by_id(self, feature_id: str) -> TypeOfFeature | None:
        """
         This function returns the first feature in the database that matches the feature_id
        """
        return self.db.query(TypeOfFeature).filter(TypeOfFeature.id == feature_id).first()

    def get_features_for_type_of_property_id(self, type_of_property_id: str) -> list:
        """
        It returns all the features for a given type of property
        """
        return self.db.query(TypeOfFeature).join(TypeOfPropertyHasFeature).filter(
            TypeOfPropertyHasFeature.type_of_property_id == type_of_property_id).all()

    def delete_by_id(self, feature_id: str) -> bool:
        """
        It deletes a feature from the database if it exists
        """
        try:
            feature = self.db.query(TypeOfFeature).filter(TypeOfFeature.id == feature_id).first()
            if feature is None:
                raise TypeOfFeatureDoesntExistException
            self.db.delete(feature)
            self.db.commit()
            return True
        except Exception as exc:
            raise exc
