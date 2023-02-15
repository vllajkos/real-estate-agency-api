from fastapi import HTTPException
from starlette.responses import JSONResponse

from app.properties.exceptions import TypeOfPropertyHasFeatureExistsException, TypeOfPropertyDoesntExistException, \
    TypeOfFeatureDoesntExistException, TypeOfPropertyDoesntHaveFeaturesException, \
    TypeOfPropertyDoesntHaveFeatureException
from app.properties.services.type_of_property_has_feature_services import TypeOfPropertyHasFeatureService


class TypeOfPropertyHasFeatureController:

    @staticmethod
    def create(type_of_property_id: str, feature_id: str):
        try:
            return TypeOfPropertyHasFeatureService.create(type_of_property_id=type_of_property_id,
                                                          feature_id=feature_id)
        except TypeOfPropertyDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except TypeOfFeatureDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except TypeOfPropertyHasFeatureExistsException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_type_of_property_with_features(type_id: str):
        try:
            return TypeOfPropertyHasFeatureService.get_type_of_property_with_features(type_of_property_id=type_id)
        except TypeOfPropertyDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except TypeOfPropertyDoesntHaveFeaturesException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def delete(type_id: str, feature_id: str):
        try:
            TypeOfPropertyHasFeatureService.delete(type_of_property_id=type_id, feature_id=feature_id)
            return JSONResponse(status_code=200, content="Type of property with feature deleted")
        except TypeOfPropertyDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except TypeOfFeatureDoesntExistException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except TypeOfPropertyDoesntHaveFeatureException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
