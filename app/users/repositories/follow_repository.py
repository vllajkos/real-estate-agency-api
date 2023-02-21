from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.exceptions import FollowDoesntExistException
from app.users.models import Follow


class FollowRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, client_id: str, advertisement_id: str):
        try:
            follow = Follow(client_id=client_id, advertisement_id=advertisement_id)
            self.db.add(follow)
            self.db.commit()
            self.db.refresh(follow)
            return follow
        except IntegrityError as err:
            raise err

    def get_all_by_client_id(self, client_id: str):
        return self.db.query(Follow).filter(Follow.client_id == client_id).all()

    def get_all_by_advertisement_id(self, advertisement_id: str):
        return self.db.query(Follow).filter(Follow.advertisement_id == advertisement_id).all()

    def get_by_client_id_and_advertisement_id(self, client_id: str, advertisement_id: str):
        return self.db.query(Follow).filter((Follow.client_id == client_id) &
                                            (Follow.advertisement_id == advertisement_id)).first()

    def delete(self, client_id: str, advertisement_id: str):
        try:
            follow = self.get_by_client_id_and_advertisement_id(client_id=client_id,
                                                                advertisement_id=advertisement_id)
            if follow:
                self.db.delete(follow)
                self.db.commit()
                return True
            raise FollowDoesntExistException
        except Exception as exc:
            raise exc
