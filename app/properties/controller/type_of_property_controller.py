from fastapi import HTTPException
from starlette.responses import JSONResponse

from app.properties.exceptions import TypeOfPropertyExistsException, TypeOfPropertyDoesntExistsException
from app.properties.services import TypeOfPropertyService


class TypeOfPropertyController:

    @staticmethod
    def create(type_of_property: str):
        try:
            return TypeOfPropertyService.create(type_of_property=type_of_property)
        except TypeOfPropertyExistsException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all():
        try:
            return TypeOfPropertyService.get_all()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_by_type_of_property(type_of_property: str):
        try:
            return TypeOfPropertyService.get_by_type_of_property(type_of_property=type_of_property)
        except TypeOfPropertyDoesntExistsException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def get_by_id(type_id: str):
        try:
            return TypeOfPropertyService.get_by_id(type_id=type_id)
        except TypeOfPropertyDoesntExistsException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def delete_by_id(type_id: str):
        try:
            TypeOfPropertyService.delete_by_id(type_id=type_id)
            return JSONResponse(status_code=200, content="Type of property deleted")
        except TypeOfPropertyDoesntExistsException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc)
