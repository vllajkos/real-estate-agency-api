from fastapi import APIRouter
from pydantic import StrictStr

from app.properties.controller import TypeOfPropertyController, TypeOfFeatureController, \
    TypeOfPropertyHasFeatureController, PropertyController
from app.properties.schemas import TypeOfPropertySchema, TypeOfPropertySchemaIn, TypeOfFeatureSchemaIn, \
    TypeOfFeatureSchemaOut, TypeOfPropertyHasFeatureSchema, PropertySchemaOut, PropertySchemaIn

type_of_property_router = APIRouter(prefix="/api/type-of-property", tags=["Type of property"])
type_of_feature_router = APIRouter(prefix="/api/type-of-feature", tags=["Type of feature"])
type_of_property_has_type_of_feature_router = APIRouter(prefix="/api/type-of-property-has-type-of-feature",
                                                        tags=["Type of property has type of feature"])
property_router = APIRouter(prefix="/api/property", tags=["Property"])

"""Type of property routes"""


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


"""Type of feature routes"""


@type_of_feature_router.post("/create", response_model=TypeOfFeatureSchemaOut)
def create_type_of_feature(type_of_feature: TypeOfFeatureSchemaIn):
    return TypeOfFeatureController.create(type_of_feature.feature)


@type_of_feature_router.get("/get-all-types", response_model=list[TypeOfFeatureSchemaOut])
def get_all_types_of_features():
    return TypeOfFeatureController.get_all()


@type_of_feature_router.get("/get-by-type/{feature}", response_model=TypeOfFeatureSchemaOut)
def get_type_of_feature_by_feature(feature: str):
    return TypeOfFeatureController.get_by_feature(feature=feature)


@type_of_feature_router.get("/get-by-id/{feature_id}", response_model=TypeOfFeatureSchemaOut)
def get_type_of_feature_by_id(feature_id: str):
    return TypeOfFeatureController.get_by_id(feature_id=feature_id)


@type_of_feature_router.get("/get-features-for-type-of-property/{type_of_property_id}",
                            response_model=list[TypeOfFeatureSchemaOut])
def get_features_for_type_of_property(type_of_property_id: str):
    return TypeOfFeatureController.get_features_for_type_of_property(type_id=type_of_property_id)


@type_of_feature_router.delete("/delete-by-id", response_model=None)
def delete_by_id(feature_id: str):
    return TypeOfFeatureController.delete_by_id(feature_id=feature_id)


""" Type of property has type of feature routes"""


@type_of_property_has_type_of_feature_router.post("/create", response_model=TypeOfPropertyHasFeatureSchema)
def create_type_of_property_has_type_of_feature(property_feature: TypeOfPropertyHasFeatureSchema):
    return TypeOfPropertyHasFeatureController.create(type_of_property_id=property_feature.type_of_property_id,
                                                     feature_id=property_feature.feature_id)


@type_of_property_has_type_of_feature_router.get("/get-type-of-property-with-all-features/{type_of_property_id}",
                                                 response_model=list[TypeOfPropertyHasFeatureSchema])
def get_type_of_property_with_all_features(type_of_property_id: str):
    return TypeOfPropertyHasFeatureController.get_type_of_property_with_features(type_id=type_of_property_id)


# @type_of_property_has_type_of_feature_router.get("/get-features-for-type-of-property/{type_of_property_id}",
#                                                  response_model=list[TypeOfFeatureSchemaOut])
# def get_features_for_type_of_property(type_of_property_id: str):
#     return TypeOfPropertyHasFeatureController.get_nesto(type_id=type_of_property_id)


@type_of_property_has_type_of_feature_router.delete("/delete", response_model=None)
def delete_feature_for_type_of_property_by_ids(type_of_property_id: str, feature_id: str):
    return TypeOfPropertyHasFeatureController.delete(type_id=type_of_property_id, feature_id=feature_id)


"""Property routes"""


@property_router.post("/create", response_model=PropertySchemaOut)
def create_property(property_: PropertySchemaIn):
    return PropertyController.create(street=property_.street, municipality=property_.municipality, city=property_.city,
                                     country=property_.country, square_meters=property_.square_meters,
                                     type_of_property_id=property_.type_of_property_id)


@property_router.get("/get-all-properties", response_model=list[PropertySchemaOut])
def get_all_properties():
    return PropertyController.get_all()


@property_router.get("/get-all-properties-for-type", response_model=list[PropertySchemaOut])
def get_all_properties_for_type_of_property_id(type_of_property_id: str):
    return PropertyController.get_all_properties_for_type_id(type_of_property_id=type_of_property_id)


@property_router.get("/get-all-properties-by-municipality", response_model=list[PropertySchemaOut])
def get_all_properties_by_municipality(municipality: str):
    return PropertyController.get_all_properties_by_municipality(municipality=municipality)


@property_router.get("/get-all-properties-by-city", response_model=list[PropertySchemaOut])
def get_all_properties_by_city(city: str):
    return PropertyController.get_all_properties_by_city(city=city)


@property_router.delete("/delete", response_model=None)
def delete_property_by_id(property_id: str):
    return PropertyController.delete(property_id=property_id)
