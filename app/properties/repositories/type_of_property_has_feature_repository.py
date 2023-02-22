"""Repository layer representing which type of property can contain which type of feature"""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.properties.exceptions import TypeOfPropertyDoesntSupportFeatureException
from app.properties.models import TypeOfPropertyHasFeature, TypeOfFeature


class TypeOfPropertyHasFeatureRepository:
    """
    This class is responsible for storing and retrieving type of property has feature objects
    """

    def __init__(self, db: Session) -> None:
        """
        Model of object with a database session
        """
        self.db = db

    def create(self, type_of_property_id: str, feature_id: str) -> TypeOfPropertyHasFeature:
        """
        It creates a new row in the TypeOfPropertyHasFeature table,
        with the type_of_property_id and feature_id passed in as
        arguments
        """
        try:
            property_feature = TypeOfPropertyHasFeature(type_of_property_id=type_of_property_id, feature_id=feature_id)
            self.db.add(property_feature)
            self.db.commit()
            self.db.refresh(property_feature)
            return property_feature
        except IntegrityError as err:
            raise err

    def get_type_of_property_with_features(self, type_of_property_id: str) -> list:
        """
        It returns all the features of a type of property
        """
        return self.db.query(TypeOfPropertyHasFeature).filter(
            TypeOfPropertyHasFeature.type_of_property_id == type_of_property_id).all()

    def get_type_of_property_with_features_by_optional_values(self, type_of_property_id: str,
                                                              optional_values: bool) -> list:
        """
        Get all the features of a type of property that have optional values.
        """
        return self.db.query(TypeOfPropertyHasFeature).join(TypeOfFeature).filter(
            (TypeOfPropertyHasFeature.type_of_property_id == type_of_property_id) &
            (TypeOfFeature.optional_values == optional_values)).all()

    def get_type_of_property_and_type_of_feature_by_ids(self, type_of_property_id: str,
                                                        feature_id: str) -> TypeOfPropertyHasFeature | None:
        """
         Get the type of property and type of feature by their ids
        """
        return self.db.query(TypeOfPropertyHasFeature).filter(
            (TypeOfPropertyHasFeature.type_of_property_id == type_of_property_id) &
            (TypeOfPropertyHasFeature.feature_id == feature_id)).first()

    def delete(self, type_of_property_id: str, feature_id: str) -> bool:
        """
        It deletes a feature from a property type
        """
        try:
            prop_feature = self.get_type_of_property_and_type_of_feature_by_ids(type_of_property_id=type_of_property_id,
                                                                                feature_id=feature_id)
            if prop_feature:
                self.db.delete(prop_feature)
                self.db.commit()
                return True
            raise TypeOfPropertyDoesntSupportFeatureException
        except Exception as exc:
            raise exc
