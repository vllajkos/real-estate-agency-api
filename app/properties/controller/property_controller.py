"""Property controller layer"""
from fastapi import HTTPException
from starlette.responses import JSONResponse
from app.properties.exceptions import TypeOfPropertyDoesntExistException, PropertiesNotFoundException, \
    PropertiesNotFoundByMunicipalityException, PropertiesNotFoundByCityException, PropertyNotFoundException, \
    CustomPropertyException
from app.properties.models import Property
from app.properties.services import PropertyService


class PropertyController:
    """Class containing Property controller methods"""

    @staticmethod
    def create(street: str, municipality: str, city: str, country: str,
               square_meters: float, type_of_property_id: str) -> Property:
        """
        It creates a property
        """
        try:
            return PropertyService.create(street=street, municipality=municipality, city=city, country=country,
                                          square_meters=square_meters, type_of_property_id=type_of_property_id)
        except TypeOfPropertyDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all() -> list:
        """
        It returns all the properties in the database
        """
        try:
            return PropertyService.get_all()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_property_by_id(property_id: str) -> Property:
        """
        This function gets a property by its id
        """
        try:
            return PropertyService.get_property_by_id(property_id=property_id)
        except PropertyNotFoundException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_properties_for_type_id(type_of_property_id: str) -> list:
        """
        It returns all properties for a given type of property id.
        """
        try:
            properties = PropertyService.get_all_properties_for_type_id(type_of_property_id=type_of_property_id)
            if properties:
                return properties
        except PropertiesNotFoundException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_properties_by_municipality(municipality: str) -> list:
        """
        It returns all properties in a given municipality
        """
        try:
            return PropertyService.get_all_properties_by_municipality(municipality=municipality)
        except PropertiesNotFoundByMunicipalityException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_properties_by_city(city: str) -> list:
        """
        It returns all properties in a given city
        """
        try:
            return PropertyService.get_all_properties_by_city(city=city)
        except PropertiesNotFoundByCityException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_properties_by_filter_parameters(municipality: str, city: str, country: str,
                                            min_square_meters: float, max_square_meters: float,
                                            type_of_property_id: str) -> list:
        """Returns properties filtered by search parameters"""
        try:
            return PropertyService.get_properties_by_filter_parameters(municipality=municipality,
                                                                       city=city, country=country,
                                                                       min_square_meters=min_square_meters,
                                                                       max_square_meters=max_square_meters,
                                                                       type_of_property_id=type_of_property_id)
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
