from fastapi import APIRouter


from app.properties.controller import TypeOfPropertyController
from app.properties.schemas import TypeOfPropertySchema, TypeOfPropertySchemaIn

type_of_property_router = APIRouter(prefix="/api/type-of-property", tags=["Type of property"])


@type_of_property_router.post("/create", response_model=TypeOfPropertySchema)
def create_type_of_property(property_type: TypeOfPropertySchemaIn):
    return TypeOfPropertyController.create(property_type.type_of_property)


@type_of_property_router.get("/get-all-types", response_model=list[TypeOfPropertySchema])
def get_all_types_of_properties():
    return TypeOfPropertyController.get_all()


@type_of_property_router.get("/get-by-type/{type_of_property}", response_model=TypeOfPropertySchema)
def get_type_of_property_by_type(type_of_property: str):
    return TypeOfPropertyController.get_by_type_of_property(type_of_property=type_of_property)


@type_of_property_router.get("/get-by-id/{type_id}", response_model=TypeOfPropertySchema)
def get_type_of_property_by_id(type_id: str):
    return TypeOfPropertyController.get_by_id(type_id=type_id)


@type_of_property_router.delete("/delete-by-id", response_model=None)
def delete_by_id(type_id: str):
    return TypeOfPropertyController.delete_by_id(type_id=type_id)
