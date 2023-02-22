""" Routes for properties, features and their related types"""
from fastapi import APIRouter
from app.properties.controller import TypeOfPropertyController, TypeOfFeatureController, \
    TypeOfPropertyHasFeatureController, PropertyController, PropertyHasFeatureController
from app.properties.schemas import TypeOfPropertySchema, TypeOfPropertySchemaIn, TypeOfFeatureSchemaIn, \
    TypeOfFeatureSchemaOut, TypeOfPropertyHasFeatureSchemaIn, PropertySchemaOut, PropertySchemaIn, \
    PropertyHasFeatureSchemaOut, PropertySchemaFilter, PropertyHasFeatureSchemaWithoutAVIn, \
    PropertyHasFeatureSchemaWithADIn, TypeOfPropertyHasFeatureSchemaOut

type_of_property_router = APIRouter(prefix="/api/type-of-property", tags=["Type of property"])


@type_of_property_router.post("/create", response_model=TypeOfPropertySchema)
def create_type_of_property(property_type: TypeOfPropertySchemaIn):
    """ Create type of property """
    return TypeOfPropertyController.create(property_type.type_of_property)


@type_of_property_router.get("/get-all-types", response_model=list[TypeOfPropertySchema])
def get_all_types_of_properties():
    """ Get all types of property """
    return TypeOfPropertyController.get_all()


@type_of_property_router.get("/get-by-type/{type_of_property}", response_model=TypeOfPropertySchema)
def get_type_of_property_by_type(type_of_property: str):
    """ Get type of property by name """
    return TypeOfPropertyController.get_by_type_of_property(type_of_property=type_of_property)


@type_of_property_router.get("/get-by-id/{type_id}", response_model=TypeOfPropertySchema)
def get_type_of_property_by_id(type_id: str):
    """ Get type of property by id """
    return TypeOfPropertyController.get_by_id(type_id=type_id)


@type_of_property_router.delete("/delete-by-id", response_model=None)
def delete_by_id(type_id: str):
    """ Delete type of property by id """
    return TypeOfPropertyController.delete_by_id(type_id=type_id)


type_of_feature_router = APIRouter(prefix="/api/type-of-feature", tags=["Type of feature"])


@type_of_feature_router.post("/create", response_model=TypeOfFeatureSchemaOut)
def create_type_of_feature(type_of_feature: TypeOfFeatureSchemaIn):
    """ Create type of feature """
    return TypeOfFeatureController.create(feature=type_of_feature.feature,
                                          optional_values=type_of_feature.optional_values)


@type_of_feature_router.get("/get-all-types", response_model=list[TypeOfFeatureSchemaOut])
def get_all_types_of_features():
    """ Get all types of features """
    return TypeOfFeatureController.get_all()


@type_of_feature_router.get("/get-by-type/{feature}", response_model=TypeOfFeatureSchemaOut)
def get_type_of_feature_by_feature(feature: str):
    """ Get type of feature by name """
    return TypeOfFeatureController.get_by_feature(feature=feature)


@type_of_feature_router.get("/get-by-id/{feature_id}", response_model=TypeOfFeatureSchemaOut)
def get_type_of_feature_by_id(feature_id: str):
    """ Get type of feature by id """
    return TypeOfFeatureController.get_by_id(feature_id=feature_id)


@type_of_feature_router.get("/get-features-for-type-of-property/{type_of_property_id}",
                            response_model=list[TypeOfFeatureSchemaOut])
def get_features_for_type_of_property(type_of_property_id: str):
    """ Get all features for type of property id """
    return TypeOfFeatureController.get_features_for_type_of_property(type_id=type_of_property_id)


@type_of_feature_router.delete("/delete-by-id", response_model=None)
def delete_by_id(feature_id: str):
    """ Delete type of feature by id """
    return TypeOfFeatureController.delete_by_id(feature_id=feature_id)


type_of_property_has_type_of_feature_router = APIRouter(prefix="/api/type-of-property-has-type-of-feature",
                                                        tags=["Type of property has type of feature"])


@type_of_property_has_type_of_feature_router.post("/create", response_model=TypeOfPropertyHasFeatureSchemaIn)
def create_type_of_property_has_type_of_feature(property_feature: TypeOfPropertyHasFeatureSchemaIn):
    """ Define which type of property can have which type of feature, connect them by their ids """
    return TypeOfPropertyHasFeatureController.create(type_of_property_id=property_feature.type_of_property_id,
                                                     feature_id=property_feature.feature_id)


@type_of_property_has_type_of_feature_router.get("/get-type-of-property-with-all-features/{type_of_property_id}",
                                                 response_model=list[TypeOfPropertyHasFeatureSchemaOut])
def get_type_of_property_with_all_features(type_of_property_id: str):
    """ Get type of property with all the features associated with type of property id """
    return TypeOfPropertyHasFeatureController.get_type_of_property_with_features(type_id=type_of_property_id)


@type_of_property_has_type_of_feature_router.get("/get-type-of-property-with-all-features-with-optional-values"
                                                 "/{type_of_property_id}",
                                                 response_model=list[TypeOfPropertyHasFeatureSchemaOut])
def get_type_of_property_with_all_features_with_optional_values(type_of_property_id: str):
    """ Get type of property with all features who can have additional value """
    return TypeOfPropertyHasFeatureController.get_type_of_property_with_features_by_optional_values(
        type_id=type_of_property_id, optional_values=True)


@type_of_property_has_type_of_feature_router.get("/get-type-of-property-with-all-features-without-optional-values"
                                                 "/{type_of_property_id}",
                                                 response_model=list[TypeOfPropertyHasFeatureSchemaOut])
def get_type_of_property_with_all_features_without_optional_values(type_of_property_id: str):
    """ Get type of property with all features who cannot have additional value """
    return TypeOfPropertyHasFeatureController.get_type_of_property_with_features_by_optional_values(
        type_id=type_of_property_id, optional_values=False)


@type_of_property_has_type_of_feature_router.delete("/delete", response_model=None)
def delete_feature_for_type_of_property_by_ids(type_of_property_id: str, feature_id: str):
    """ Delete feature associated with type of property by their ids """
    return TypeOfPropertyHasFeatureController.delete(type_id=type_of_property_id, feature_id=feature_id)


property_router = APIRouter(prefix="/api/property", tags=["Property"])


@property_router.post("/create", response_model=PropertySchemaOut)
def create_property(property_: PropertySchemaIn):
    """ Create property """
    return PropertyController.create(street=property_.street, municipality=property_.municipality, city=property_.city,
                                     country=property_.country, square_meters=property_.square_meters,
                                     type_of_property_id=property_.type_of_property_id)


@property_router.get("/get-all-properties", response_model=list[PropertySchemaOut])
def get_all_properties():
    """ Get all properties """
    return PropertyController.get_all()


@property_router.get("/get-property-by-id/{property_id}", response_model=PropertySchemaOut)
def get_property_by_id(property_id: str):
    """ Get property by id """
    return PropertyController.get_property_by_id(property_id=property_id)


@property_router.get("/get-all-properties-for-type", response_model=list[PropertySchemaOut])
def get_all_properties_for_type_of_property_id(type_of_property_id: str):
    """ Get all properties by type of property id """
    return PropertyController.get_all_properties_for_type_id(type_of_property_id=type_of_property_id)


@property_router.post("/get-all-properties-by-filter-parameters", response_model=None)
def get_properties_by_filter_parameters(filter_para: PropertySchemaFilter):
    """ Filter properties by optional parameters """
    return PropertyController.get_properties_by_filter_parameters(municipality=filter_para.municipality,
                                                                  city=filter_para.city, country=filter_para.country,
                                                                  min_square_meters=filter_para.min_square_meters,
                                                                  max_square_meters=filter_para.max_square_meters,
                                                                  type_of_property_id=filter_para.type_of_property_id)


@property_router.get("/get-all-properties-by-municipality", response_model=list[PropertySchemaOut])
def get_all_properties_by_municipality(municipality: str):
    """ Get all properties by municipality """
    return PropertyController.get_all_properties_by_municipality(municipality=municipality)


@property_router.get("/get-all-properties-by-city", response_model=list[PropertySchemaOut])
def get_all_properties_by_city(city: str):
    """ Get all properties by city """
    return PropertyController.get_all_properties_by_city(city=city)


@property_router.delete("/delete", response_model=None)
def delete_property_by_id(property_id: str):
    """ Delete property """
    return PropertyController.delete(property_id=property_id)


property_has_feature_router = APIRouter(prefix="/api/property-has-feature", tags=["Property has feature"])


@property_has_feature_router.post("/create-property-has-feature-with-additional-value",
                                  response_model=PropertyHasFeatureSchemaOut)
def create_property_has_feature_with_additional_value(property_feature: PropertyHasFeatureSchemaWithADIn):
    """ Add to existing property feature that have additional value"""
    return PropertyHasFeatureController.create(property_id=property_feature.property_id,
                                               feature_id=property_feature.feature_id,
                                               additional_feature_value=property_feature.additional_feature_value)


@property_has_feature_router.post("/create-property-has-feature-without-additional-value",
                                  response_model=PropertyHasFeatureSchemaOut)
def create_property_has_feature_without_additional_value(property_feature: PropertyHasFeatureSchemaWithoutAVIn):
    """ Add to existing property feature without additional value"""
    return PropertyHasFeatureController.create(property_id=property_feature.property_id,
                                               feature_id=property_feature.feature_id,
                                               additional_feature_value=None)


@property_has_feature_router.get("/get-all-features-for-property-by-id/{property_id}",
                                 response_model=list[PropertyHasFeatureSchemaOut])
def get_all_features_for_property_by_id(property_id: str):
    """ Get all features for existing property by id """
    return PropertyHasFeatureController.get_all_features_for_property_by_id(property_id=property_id)


@property_has_feature_router.delete("/delete-feature-from-property-by-ids", response_model=None)
def delete_feature_from_property_by_ids(property_id: str, feature_id: str):
    """ Delete feature from property by their ids """
    return PropertyHasFeatureController.delete_feature_from_property_by_ids(property_id=property_id,
                                                                            feature_id=feature_id)
