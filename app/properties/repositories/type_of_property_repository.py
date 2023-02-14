from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.properties.exceptions import TypeOfPropertyDoesntExistsException
from app.properties.models import TypeOfProperty


class TypeOfPropertyRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, type_of_property: str):
        try:
            property_type = TypeOfProperty(type_of_property=type_of_property)
            self.db.add(property_type)
            self.db.commit()
            self.db.refresh(property_type)
            return property_type
        except IntegrityError as err:
            raise err

    def get_by_type_of_property(self, type_of_property: str):
        return self.db.query(TypeOfProperty).filter(TypeOfProperty.type_of_property == type_of_property).first()

    def get_all(self):
        return self.db.query(TypeOfProperty).all()

    def get_by_id(self, type_id: str):
        return self.db.query(TypeOfProperty).filter(TypeOfProperty.id == type_id).first()

    def delete_by_id(self, type_id: str):
        try:
            type_of_property = self.db.query(TypeOfProperty).filter(TypeOfProperty.id == type_id).first()
            if type_of_property is None:
                raise TypeOfPropertyDoesntExistsException
            self.db.delete(type_of_property)
            self.db.commit()
            return True
        except Exception as exc:
            raise exc
