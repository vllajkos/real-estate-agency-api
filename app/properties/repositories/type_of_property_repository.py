"""Repository layer for managing type of property with connection to database"""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.properties.exceptions import TypeOfPropertyDoesntExistException, TypeOfPropertyDeleteException
from app.properties.models import TypeOfProperty


class TypeOfPropertyRepository:
    """This class is a repository for the TypeOfProperty class."""
    def __init__(self, db: Session) -> None:
        """
        Session object
        """
        self.db = db

    def create(self, type_of_property: str) -> TypeOfProperty:
        """
        It creates a new property type
        """
        try:
            property_type = TypeOfProperty(type_of_property=type_of_property)
            self.db.add(property_type)
            self.db.commit()
            self.db.refresh(property_type)
            return property_type
        except IntegrityError as err:
            raise err

    def get_by_type_of_property(self, type_of_property: str) -> TypeOfProperty | None:
        """
        It returns the first instance of the TypeOfProperty class where the type_of_property attribute is equal to the
        type_of_property argument
        """
        return self.db.query(TypeOfProperty).filter(TypeOfProperty.type_of_property == type_of_property).first()

    def get_all(self) -> list:
        """
        It returns all the rows in the TypeOfProperty table
        """
        return self.db.query(TypeOfProperty).all()

    def get_by_id(self, type_id: str) -> TypeOfProperty | None:
        """
        It returns the first row of the TypeOfProperty table where the id column is equal to the type_id parameter
        """
        return self.db.query(TypeOfProperty).filter(TypeOfProperty.id == type_id).first()

    def delete_by_id(self, type_id: str) -> bool:
        """
        It deletes a type of property from the database
        """
        try:
            type_of_property = self.db.query(TypeOfProperty).filter(TypeOfProperty.id == type_id).first()
            if type_of_property is None:
                raise TypeOfPropertyDoesntExistException
            self.db.delete(type_of_property)
            self.db.commit()
            return True
        except IntegrityError:
            raise TypeOfPropertyDeleteException
        except Exception as exc:
            raise exc
