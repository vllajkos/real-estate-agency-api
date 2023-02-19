from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.properties.exceptions import PropertyNotFoundException, MinMaxSquareMetersException
from app.properties.models import Property


class PropertyRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, street: str, municipality: str, city: str, country: str, square_meters: float,
               type_of_property_id: str):
        try:
            property_ = Property(street=street, municipality=municipality, city=city, country=country,
                                 square_meters=square_meters, type_of_property_id=type_of_property_id)
            self.db.add(property_)
            self.db.commit()
            self.db.refresh(property_)
            return property_
        except IntegrityError as err:
            raise err

    def get_all(self):
        return self.db.query(Property).all()

    def get_property_by_id(self, property_id: str):
        return self.db.query(Property).filter(Property.id == property_id).first()

    def get_all_properties_for_type_id(self, type_of_property_id: str):
        return self.db.query(Property).filter(Property.type_of_property_id == type_of_property_id).all()

    def get_all_properties_by_municipality(self, municipality: str):
        return self.db.query(Property).filter(Property.city.ilike(f"%{municipality}%")).all()

    def get_all_properties_by_city(self, city: str):
        return self.db.query(Property).filter(Property.city.ilike(f"%{city}%")).all()

    def get_properties_by_filter_parameters(self, municipality: str, city: str, country: str,
                                            min_square_meters: float, max_square_meters: float,
                                            type_of_property_id: str):
        # returns for all none variables filtered properties by filter parameters
        query = self.db.query(Property)
        if municipality:
            query = query.filter(Property.municipality == municipality)
        if city:
            query = query.filter(Property.city.ilike(city))
        if country:
            query = query.filter(Property.country == country)

        if min_square_meters and max_square_meters:
            if min_square_meters > max_square_meters:
                raise MinMaxSquareMetersException
            query = query.filter(Property.square_meters.between(min_square_meters, max_square_meters))
        elif min_square_meters:
            query = query.filter(Property.square_meters > min_square_meters)
        elif max_square_meters:
            query = query.filter(Property.square_meters < max_square_meters)
        if type_of_property_id:
            query = query.filter(Property.type_of_property_id == type_of_property_id)
        return query.all()

    def get_properties_ids_by_filter_parameters(self, municipality: str, city: str, country: str,
                                                min_square_meters: float, max_square_meters: float,
                                                type_of_property_id: str) -> list:
        # returns for all none variables filtered property's ids by filter parameters as single tuple list
        query = self.db.query(Property.id)
        if municipality:
            query = query.filter(Property.municipality == municipality)
        if city:
            query = query.filter(Property.city == city)
        if country:
            query = query.filter(Property.country == country)

        if min_square_meters and max_square_meters:
            if min_square_meters > max_square_meters:
                raise MinMaxSquareMetersException
            query = query.filter(Property.square_meters.between(min_square_meters, max_square_meters))
        elif min_square_meters:
            query = query.filter(Property.square_meters > min_square_meters)
        elif max_square_meters:
            query = query.filter(Property.square_meters < max_square_meters)
        if type_of_property_id:
            query = query.filter(Property.type_of_property_id == type_of_property_id)
        return query.all()

    def delete(self, property_id: str):
        try:
            property_ = self.db.query(Property).filter(Property.id == property_id).first()
            if property_:
                self.db.delete(property_)
                self.db.commit()
                return
            raise PropertyNotFoundException
        except Exception as exc:
            raise exc
