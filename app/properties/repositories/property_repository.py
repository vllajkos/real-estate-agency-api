from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.properties.exceptions import PropertyNotFoundException
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
