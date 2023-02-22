"""User repository layer"""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import CannotDeleteInUseException, UserIdDoesntExistException
from app.users.models import User


class UserRepository:
    """This class is responsible for retrieving users from the database"""

    def __init__(self, db: Session) -> None:
        """Repository object"""
        self.db = db

    def create_user(self, username: str, email: str, password: str) -> User:
        """Creates user"""
        try:
            user = User(username=username, email=email, password=password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as err:
            raise err

    def create_superuser(self, username: str, email: str, password: str) -> User:
        """Creates superuser"""
        try:
            user = User(username=username, email=email, password=password, superuser=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as err:
            raise err

    def get_by_username(self, username: str) -> User | None:
        """
        It returns the first user in the database whose username matches the username passed in as an argument
        """
        return self.db.query(User).filter(User.username == username).first()

    def get_by_email(self, email: str) -> User | None:
        """
        It returns the first user in the database whose email matches the email passed in as an argument
        """
        return self.db.query(User).filter(User.email == email).first()

    def get_by_username_or_email(self, username_or_email: str):
        """
        It returns the first user that matches the username or email
        """
        return (
            self.db.query(User).filter((User.email == username_or_email) | (User.username == username_or_email)).first()
        )

    def get_user_by_id(self, user_id: str) -> User | None:
        """
        This function returns the first user in the database with the given user_id
        """
        return self.db.query(User).filter(User.id == user_id).first()

    def get_all_active_users(self) -> list:
        """
        It returns all the users from the database who have an active status of 1
        """
        return self.db.query(User).filter(User.active_status == 1).all()

    def get_all_users(self) -> list:
        """
        It returns all the users in the database
        """
        return self.db.query(User).all()

    def delete(self, user_id: str) -> None:
        """
        It deletes a user from the database if the user exists
        """
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user:
                self.db.delete(user)
                self.db.commit()
                return
            raise UserIdDoesntExistException
        except IntegrityError:
            raise CannotDeleteInUseException
        except Exception as exc:
            raise exc

    def update_user_active_status(self, user_id: str, active_status: bool) -> [User]:
        """
        It updates the active status of a user in the database
        """
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user:
                user.active_status = active_status
                self.db.add(user)
                self.db.commit()
                self.db.refresh(user)
                return user
            raise UserIdDoesntExistException
        except Exception as exc:
            raise exc
