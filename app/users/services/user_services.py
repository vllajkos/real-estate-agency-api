import hashlib
from app.db.database import SessionLocal
from app.users.exceptions import InvalidUsernameException, InvalidEmailException, UserIdDoesntExistException, \
    InvalidPasswordException, InvalidLoginInfoException

from app.users.repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    def create_user(username: str, email: str, password: str):
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
    def create_superuser(username: str, email: str, password: str):
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
    def get_user_by_id(user_id: str):
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.get_user_by_id(user_id=user_id)
            if user:
                return user
            raise UserIdDoesntExistException

    @staticmethod
    def get_all_users():
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all_users()

    @staticmethod
    def get_all_active_users():
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all_active_users()

    @staticmethod
    def delete(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                if user_repository.get_user_by_id(user_id=user_id):
                    return user_repository.delete(user_id)
                raise UserIdDoesntExistException
        except Exception as exc:
            raise exc

    @staticmethod
    def update_user_active_status(user_id: str, active_status: bool):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                if user_repository.get_user_by_id(user_id=user_id):
                    return user_repository.update_user_active_status(user_id=user_id, active_status=active_status)
                raise UserIdDoesntExistException
            except Exception as exc:
                raise exc

    @staticmethod
    def login_user(username_or_email: str, password: str):
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
