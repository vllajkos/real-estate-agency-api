from app.db import SessionLocal
from app.properties.exceptions import TypeOfFeatureExistsException, TypeOfFeatureDoesntExistException
from app.properties.repositories import TypeOfFeatureRepository


class TypeOfFeatureService:

    @staticmethod
    def create(feature: str):
        with SessionLocal() as db:
            try:
                feature_repository = TypeOfFeatureRepository(db=db)
                if feature_repository.get_by_feature(feature=feature):
                    raise TypeOfFeatureExistsException
                return feature_repository.create(feature=feature)
            except Exception as exc:
                raise exc

    @staticmethod
    def get_all():
        with SessionLocal() as db:
            try:
                feature_repository = TypeOfFeatureRepository(db=db)
                return feature_repository.get_all()
            except Exception as exc:
                raise exc

    @staticmethod
    def get_by_feature(feature: str):
        with SessionLocal() as db:
            feature_repository = TypeOfFeatureRepository(db=db)
            feature_obj = feature_repository.get_by_feature(feature=feature)
            if feature_obj is None:
                raise TypeOfFeatureDoesntExistException
            return feature_obj

    @staticmethod
    def get_by_id(feature_id: str):
        with SessionLocal() as db:
            feature_repository = TypeOfFeatureRepository(db=db)
            feature_obj = feature_repository.get_by_id(feature_id=feature_id)
            if feature_obj is None:
                raise TypeOfFeatureDoesntExistException
            return feature_obj

    @staticmethod
    def delete_by_id(feature_id: str):
        with SessionLocal() as db:
            try:
                feature_repository = TypeOfFeatureRepository(db=db)
                feature_repository.delete_by_id(feature_id=feature_id)
            except Exception as exc:
                raise exc
