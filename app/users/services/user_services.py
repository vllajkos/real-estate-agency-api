"""User service layer"""
import hashlib
from app.db.database import SessionLocal
from app.users.exceptions import InvalidUsernameException, InvalidEmailException, UserIdDoesntExistException, \
    InvalidPasswordException, InvalidLoginInfoException
from app.users.models import User
from app.users.repositories.user_repository import UserRepository


class UserService:
    """Class containing user service layer methods"""
    @staticmethod
    def create_user(username: str, email: str, password: str) -> User:
        """
        It creates a user in the database
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                if user_repository.get_by_username(username=username):
                    raise InvalidUsernameException
                if user_repository.get_by_email(email=email):
                    raise InvalidEmailException
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(username=username, email=email, password=hashed_password)
            except Exception as exc:
                raise exc

    @staticmethod
    def create_superuser(username: str, email: str, password: str) -> User:
        """
        It creates a superuser
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                if user_repository.get_by_username(username=username):
                    raise InvalidUsernameException
                if user_repository.get_by_email(email=email):
                    raise InvalidEmailException
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_superuser(username=username, email=email, password=hashed_password)
            except Exception as exc:
                raise exc

    @staticmethod
    def get_user_by_id(user_id: str) -> User:
        """
        This function gets a user by id from the database
        """
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.get_user_by_id(user_id=user_id)
            if user:
                return user
            raise UserIdDoesntExistException

    @staticmethod
    def get_all_users() -> list:
        """
        It gets all users from the database
        """
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all_users()

    @staticmethod
    def get_all_active_users() -> list:
        """
        "Get all active users from the database."
        """
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all_active_users()

    @staticmethod
    def delete(user_id: str) -> None:
        """
        It deletes a user from the database if the user exists
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                if user_repository.get_user_by_id(user_id=user_id):
                    return user_repository.delete(user_id)
                raise UserIdDoesntExistException
        except Exception as exc:
            raise exc

    @staticmethod
    def update_user_active_status(user_id: str, active_status: bool) -> User:
        """
        It updates the active status of a user in the database
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                if user_repository.get_user_by_id(user_id=user_id):
                    return user_repository.update_user_active_status(user_id=user_id, active_status=active_status)
                raise UserIdDoesntExistException
            except Exception as exc:
                raise exc

    @staticmethod
    def login_user(username_or_email: str, password: str) -> User:
        """
        It takes a username or email and a password, and returns a user if the username or email and password are valid
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.get_by_username_or_email(username_or_email=username_or_email)
                if user:
                    if hashlib.sha256(bytes(password, "utf-8")).hexdigest() == user.password:
                        return user
                    raise InvalidPasswordException
                raise InvalidLoginInfoException
            except Exception as exc:
                raise exc
