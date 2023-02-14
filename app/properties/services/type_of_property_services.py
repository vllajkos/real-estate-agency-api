from app.db import SessionLocal
from app.properties.exceptions import TypeOfPropertyExistsException, TypeOfPropertyDoesntExistsException
from app.properties.repositories import TypeOfPropertyRepository


class TypeOfPropertyService:

    @staticmethod
    def create(type_of_property: str):
        with SessionLocal() as db:
            try:
                type_of_property_repository = TypeOfPropertyRepository(db=db)
                if type_of_property_repository.get_by_type_of_property(type_of_property=type_of_property):
                    raise TypeOfPropertyExistsException
                return type_of_property_repository.create(type_of_property=type_of_property)
            except Exception as exc:
                raise exc

    @staticmethod
    def get_all():
        with SessionLocal() as db:
            try:
                type_of_property_repository = TypeOfPropertyRepository(db=db)
                return type_of_property_repository.get_all()
            except Exception as exc:
                raise exc

    @staticmethod
    def get_by_type_of_property(type_of_property: str):
        with SessionLocal() as db:
            type_of_property_repository = TypeOfPropertyRepository(db=db)
            property_type = type_of_property_repository.get_by_type_of_property(type_of_property=type_of_property)
            if property_type is None:
                raise TypeOfPropertyDoesntExistsException
            return property_type

    @staticmethod
    def get_by_id(type_id: str):
        with SessionLocal() as db:
            type_of_property_repository = TypeOfPropertyRepository(db=db)
            property_type = type_of_property_repository.get_by_id(type_id=type_id)
            if property_type is None:
                raise TypeOfPropertyDoesntExistsException
            return property_type

    @staticmethod
    def delete_by_id(type_id: str):
        with SessionLocal() as db:
            try:
                type_of_property_repository = TypeOfPropertyRepository(db=db)
                type_of_property_repository.delete_by_id(type_id=type_id)
            except Exception as exc:
                raise exc
