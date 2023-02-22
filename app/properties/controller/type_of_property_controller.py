"""Type of property controller layer"""
from fastapi import HTTPException
from starlette.responses import JSONResponse
from app.properties.exceptions import TypeOfPropertyExistsException, TypeOfPropertyDoesntExistException, \
    CustomPropertyException
from app.properties.models import TypeOfProperty
from app.properties.services import TypeOfPropertyService


class TypeOfPropertyController:
    """Class containing Type of property controller methods"""
    @staticmethod
    def create(type_of_property: str) -> TypeOfProperty:
        """
        It creates a new type of property
        """
        try:
            return TypeOfPropertyService.create(type_of_property=type_of_property)
        except TypeOfPropertyExistsException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all() -> list:
        """
        It returns all the TypeOfProperty objects from the database
        """
        try:
            return TypeOfPropertyService.get_all()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_by_type_of_property(type_of_property: str) -> TypeOfProperty:
        """
        It returns a TypeOfProperty object if the type_of_property exists, otherwise it raises an HTTPException
        """
        try:
            return TypeOfPropertyService.get_by_type_of_property(type_of_property=type_of_property)
        except TypeOfPropertyDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def get_by_id(type_id: str) -> TypeOfProperty:
        """
        It gets the type of property by id.
        """
        try:
            return TypeOfPropertyService.get_by_id(type_id=type_id)
        except TypeOfPropertyDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def delete_by_id(type_id: str) -> JSONResponse:
        """
        It deletes a type of property by its id
        """
        try:
            TypeOfPropertyService.delete_by_id(type_id=type_id)
            return JSONResponse(status_code=200, content="Type of property deleted")
        except CustomPropertyException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
