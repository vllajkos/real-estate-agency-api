from fastapi import HTTPException
from starlette.responses import JSONResponse

from app.properties.exceptions import TypeOfPropertyDoesntExistException, PropertiesNotFoundException, \
    PropertiesNotFoundByMunicipalityException, PropertiesNotFoundByCityException, PropertyNotFoundException, \
    CustomPropertyException
from app.properties.services import PropertyService


class PropertyController:

    @staticmethod
    def create(street: str, municipality: str, city: str, country: str, square_meters: float, type_of_property_id: str):
        try:
            return PropertyService.create(street=street, municipality=municipality, city=city, country=country,
                                          square_meters=square_meters, type_of_property_id=type_of_property_id)
        except TypeOfPropertyDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all():
        try:
            return PropertyService.get_all()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_property_by_id(property_id: str):
        try:
            return PropertyService.get_property_by_id(property_id=property_id)
        except PropertyNotFoundException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_properties_for_type_id(type_of_property_id: str):
        try:
            properties = PropertyService.get_all_properties_for_type_id(type_of_property_id=type_of_property_id)
            if properties:
                return properties
        except PropertiesNotFoundException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_properties_by_municipality(municipality: str):
        try:
            return PropertyService.get_all_properties_by_municipality(municipality=municipality)
        except PropertiesNotFoundByMunicipalityException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_properties_by_city(city: str):
        try:
            return PropertyService.get_all_properties_by_city(city=city)
        except PropertiesNotFoundByCityException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_properties_by_filter_parameters(municipality: str, city: str, country: str,
                                            min_square_meters: float, max_square_meters: float,
                                            type_of_property_id: str):
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

    @staticmethod
    def delete(property_id: str):
        try:
            PropertyService.delete(property_id=property_id)
            return JSONResponse(status_code=200, content="Property successfully deleted")
        except PropertyNotFoundException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
