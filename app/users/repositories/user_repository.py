from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import UserIdDoesntExistException
from app.users.models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, email: str, password: str):
        try:
            user = User(username=username, email=email, password=password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as err:
            raise err

    def create_superuser(self, username: str, email: str, password: str):
        try:
            user = User(username=username, email=email, password=password, superuser=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as err:
            raise err

    def get_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_by_username_or_email(self, username_or_email: str):
        return self.db.query(User).filter(
            (User.email == username_or_email) | (User.username == username_or_email)).first()

    def get_user_by_id(self, user_id: str):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_all_active_users(self):
        return self.db.query(User).filter(User.active_status == 1).all()

    def get_all_users(self):
        return self.db.query(User).all()

    def delete(self, user_id: str):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user:
                self.db.delete(user)
                self.db.commit()
                return
            raise UserIdDoesntExistException
        except Exception as exc:
            raise exc

    def update_user_active_status(self, user_id: str, active_status: bool):
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
