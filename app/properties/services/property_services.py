from app.db import SessionLocal
from app.properties.exceptions import PropertiesNotFoundException, PropertiesNotFoundByMunicipalityException, \
    PropertiesNotFoundByCityException
from app.properties.repositories import PropertyRepository, TypeOfPropertyRepository
from app.properties.services import TypeOfPropertyService


class PropertyService:

    @staticmethod
    def create(street: str, municipality: str, city: str, country: str, square_meters: float, type_of_property_id: str):
        try:
            with SessionLocal() as db:
                TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
                property_repo = PropertyRepository(db)
                return property_repo.create(street=street, municipality=municipality, city=city, country=country,
                                            square_meters=square_meters, type_of_property_id=type_of_property_id)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all():
        try:
            with SessionLocal() as db:
                property_repo = PropertyRepository(db=db)
                return property_repo.get_all()
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_properties_for_type_id(type_of_property_id: str):
        try:
            with SessionLocal() as db:
                property_repo = PropertyRepository(db=db)
                properties = property_repo.get_all_properties_for_type_id(type_of_property_id=type_of_property_id)
                if properties:
                    return properties
                raise PropertiesNotFoundException
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_properties_by_municipality(municipality: str):
        try:
            with SessionLocal() as db:
                property_repo = PropertyRepository(db)
                properties = property_repo.get_all_properties_by_municipality(municipality=municipality)
                if properties:
                    return properties
                raise PropertiesNotFoundByMunicipalityException
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_properties_by_city(city: str):
        try:
            with SessionLocal() as db:
                property_repo = PropertyRepository(db)
                properties = property_repo.get_all_properties_by_city(city=city)
                if properties:
                    return properties
                raise PropertiesNotFoundByCityException
        except Exception as exc:
            raise exc

    @staticmethod
    def delete(property_id: str):
        try:
            with SessionLocal() as db:
                property_repo = PropertyRepository(db)
                property_repo.delete(property_id=property_id)
        except Exception as exc:
            raise exc
