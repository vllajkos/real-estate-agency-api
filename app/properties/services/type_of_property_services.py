""" Service layer for types of properties"""
from app.db import SessionLocal
from app.properties.exceptions import TypeOfPropertyDoesntExistException, TypeOfPropertyExistsException
from app.properties.models import TypeOfProperty
from app.properties.repositories import TypeOfPropertyRepository


class TypeOfPropertyService:
    """Class containing methods of a service layer for types of properties"""

    @staticmethod
    def create(type_of_property: str) -> TypeOfProperty:
        """
        It creates a new type of property if it doesn't already exist
        """
        try:
            with SessionLocal() as db:
                type_of_property_repository = TypeOfPropertyRepository(db=db)
                if type_of_property_repository.get_by_type_of_property(type_of_property=type_of_property):
                    raise TypeOfPropertyExistsException
                return type_of_property_repository.create(type_of_property=type_of_property)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all() -> list:
        """
        It gets all the type of properties from the database
        """
        try:
            with SessionLocal() as db:
                type_of_property_repository = TypeOfPropertyRepository(db=db)
                return type_of_property_repository.get_all()
        except Exception as exc:
            raise exc

    @staticmethod
    def get_by_type_of_property(type_of_property: str) -> TypeOfProperty:
        """
        It gets a type of property by its type of property
        """
        with SessionLocal() as db:
            type_of_property_repository = TypeOfPropertyRepository(db=db)
            property_type = type_of_property_repository.get_by_type_of_property(type_of_property=type_of_property)
            if property_type is None:
                raise TypeOfPropertyDoesntExistException
            return property_type

    @staticmethod
    def get_by_id(type_id: str) -> TypeOfProperty:
        """
        It gets a property type by its id
        """
        with SessionLocal() as db:
            type_of_property_repository = TypeOfPropertyRepository(db=db)
            property_type = type_of_property_repository.get_by_id(type_id=type_id)
            if property_type is None:
                raise TypeOfPropertyDoesntExistException
            return property_type

    @staticmethod
    def delete_by_id(type_id: str) -> None:
        """
        It deletes a type of property by its id
        """
        try:
            with SessionLocal() as db:
                type_of_property_repository = TypeOfPropertyRepository(db=db)
                type_of_property_repository.delete_by_id(type_id=type_id)
        except Exception as exc:
            raise exc
