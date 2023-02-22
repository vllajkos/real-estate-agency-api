"""Service layer of a property"""
from app.db import SessionLocal
from app.properties.exceptions import PropertiesNotFoundException, PropertiesNotFoundByMunicipalityException, \
    PropertiesNotFoundByCityException, PropertyNotFoundException, PropertiesNotFoundByFilterParametersException
from app.properties.models import Property
from app.properties.repositories import PropertyRepository
from app.properties.services import TypeOfPropertyService


class PropertyService:
    """Class containing methods from service layer of a property"""
    @staticmethod
    def create(street: str, municipality: str, city: str, country: str,
               square_meters: float, type_of_property_id: str) -> Property:
        """
        It creates a property in the database
        """
        try:
            with SessionLocal() as db:
                TypeOfPropertyService.get_by_id(type_id=type_of_property_id)
                property_repo = PropertyRepository(db)
                return property_repo.create(street=street, municipality=municipality, city=city, country=country,
                                            square_meters=square_meters, type_of_property_id=type_of_property_id)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all() -> list:
        """
        It gets all the properties from the database
        """
        try:
            with SessionLocal() as db:
                property_repo = PropertyRepository(db=db)
                return property_repo.get_all()
        except Exception as exc:
            raise exc

    @staticmethod
    def get_property_by_id(property_id: str) -> Property | None:
        """
         This function gets a property by its id
        """
        try:
            with SessionLocal() as db:
                property_repo = PropertyRepository(db=db)
                property_ = property_repo.get_property_by_id(property_id=property_id)
                if property_:
                    return property_
                raise PropertyNotFoundException
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_properties_for_type_id(type_of_property_id: str) -> list:
        """
        It gets all properties for a given type of property id
        """
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
    def get_all_properties_by_municipality(municipality: str) -> list:
        """
        It gets all properties by municipality
        """
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
    def get_all_properties_by_city(city: str) -> list:
        """
        It gets all properties by city
        """
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
    def get_properties_by_filter_parameters(municipality: str, city: str, country: str,
                                            min_square_meters: float, max_square_meters: float,
                                            type_of_property_id: str) -> list:
        """Returns properties found by filter parameters"""
        try:
            with SessionLocal() as db:
                property_repo = PropertyRepository(db)
                prop_ids = property_repo.get_properties_by_filter_parameters(municipality=municipality,
                                                                             city=city, country=country,
                                                                             min_square_meters=min_square_meters,
                                                                             max_square_meters=max_square_meters,
                                                                             type_of_property_id=type_of_property_id)
                if prop_ids:
                    return prop_ids
                raise PropertiesNotFoundByFilterParametersException
        except Exception as exc:
            raise exc

    @staticmethod
    def get_properties_ids_by_filter_parameters(municipality: str, city: str, country: str,
                                                min_square_meters: float, max_square_meters: float,
                                                type_of_property_id: str) -> list:
        """ Returns list of properties ids by filter parameters"""
        try:
            with SessionLocal() as db:
                property_repo = PropertyRepository(db)
                pr_ids = property_repo.get_properties_ids_by_filter_parameters(municipality=municipality,
                                                                               city=city, country=country,
                                                                               min_square_meters=min_square_meters,
                                                                               max_square_meters=max_square_meters,
                                                                               type_of_property_id=type_of_property_id)
                if pr_ids:
                    return pr_ids
                raise PropertiesNotFoundByFilterParametersException
        except Exception as exc:
            raise exc
