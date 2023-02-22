"""Follow Repository layer"""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import FollowDoesntExistException
from app.users.models import Follow


class FollowRepository:
    """Class with follow repository methods for connecting with database"""

    def __init__(self, db: Session) -> None:
        """Repository object"""
        self.db = db

    def create(self, client_id: str, advertisement_id: str) -> Follow:
        """
        It creates a new follow object and adds it to the database
        """
        try:
            follow = Follow(client_id=client_id, advertisement_id=advertisement_id)
            self.db.add(follow)
            self.db.commit()
            self.db.refresh(follow)
            return follow
        except IntegrityError as err:
            raise err

    def get_all_by_client_id(self, client_id: str) -> list:
        """
        It returns all the rows in the Follow table where the client_id column matches the client_id parameter
        """
        return self.db.query(Follow).filter(Follow.client_id == client_id).all()

    def get_all_by_advertisement_id(self, advertisement_id: str) -> list:
        """
        It returns all the rows in the Follow table where the advertisement_id column is equal to the advertisement_id
        parameter.
        """
        return self.db.query(Follow).filter(Follow.advertisement_id == advertisement_id).all()

    def get_by_client_id_and_advertisement_id(self, client_id: str, advertisement_id: str) -> Follow | None:
        """
        It returns the first row from the Follow table where the client_id
        and advertisement_id match the given parameters
        """
        return (
            self.db.query(Follow)
            .filter((Follow.client_id == client_id) & (Follow.advertisement_id == advertisement_id))
            .first()
        )

    def delete(self, client_id: str, advertisement_id: str) -> None:
        """
        Unfollows ad by user by removing it from the database if it exists, otherwise it raises an exception
        """
        try:
            follow = self.get_by_client_id_and_advertisement_id(client_id=client_id, advertisement_id=advertisement_id)
            if follow:
                self.db.delete(follow)
                self.db.commit()
                return
            raise FollowDoesntExistException
        except Exception as exc:
            raise exc
