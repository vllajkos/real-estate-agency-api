"""
Repository layer for concrete property having features
"""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.properties.exceptions import PropertyDoesntHaveRequestedFeatureException
from app.properties.models import PropertyHasFeature


class PropertyHasFeatureRepository:
    """Model of concrete property having features"""

    def __init__(self, db: Session) -> None:
        """Model for PropertyHasFeatureRepository object"""
        self.db = db

    def create(self, property_id: str, feature_id: str, additional_feature_value: int):
        """
        It creates a new row in the PropertyHasFeature table, with the given property_id, feature_id, and
        additional_feature_value
        """
        try:
            property_feature = PropertyHasFeature(property_id=property_id, feature_id=feature_id,
                                                  additional_feature_value=additional_feature_value)
            self.db.add(property_feature)
            self.db.commit()
            self.db.refresh(property_feature)
            return property_feature
        except IntegrityError as err:
            raise err

    def get_property_with_feature_by_ids(self, property_id: str, feature_id: str) -> PropertyHasFeature | None:
        """
        Get the property with feature by ids
        """
        return self.db.query(PropertyHasFeature).filter((PropertyHasFeature.property_id == property_id) &
                                                        (PropertyHasFeature.feature_id == feature_id)).first()

    def get_all_features_for_property_by_id(self, property_id: str) -> list:
        """
        This function returns all the features for a property by its id
        """
        return self.db.query(PropertyHasFeature).filter(PropertyHasFeature.property_id == property_id).all()

    def get_properties_ids_by_filter_parameters(self, features_id_list: list[str]) -> list:
        """
        It returns a list of tuples containing the property_id of each property that has a feature_id that is in the
        features_id_list
        """
        # returns filtered property's ids by filter parameters as single element tuple list
        return self.db.query(PropertyHasFeature.property_id).filter(
            PropertyHasFeature.feature_id.in_(features_id_list)).all()

    def get_properties_by_features_list(self, features_id_list: list) -> list:
        """
         It returns a list of all the properties that have at least one of the features in the features_id_list
        """
        return self.db.query(PropertyHasFeature).filter(PropertyHasFeature.feature_id.in_(features_id_list)).all()

    def delete_feature_from_property_by_ids(self, property_id: str, feature_id: str) -> None:
        """
        It deletes a feature from a property by ids
        """
        try:
            property_has_feature = self.get_property_with_feature_by_ids(property_id=property_id, feature_id=feature_id)
            if property_has_feature:
                self.db.delete(property_has_feature)
                self.db.commit()
                return
            raise PropertyDoesntHaveRequestedFeatureException
        except Exception as exc:
            raise exc
