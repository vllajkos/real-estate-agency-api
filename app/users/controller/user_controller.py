"""User controller layer"""
from fastapi import HTTPException
from starlette.responses import JSONResponse
from app.users.exceptions import CustomUserException
from app.users.models import User
from app.users.services import UserService, signJWT


class UserController:
    """Class containing User controller methods"""

    @staticmethod
    def create_user(username: str, email: str, password: str) -> User:
        """
        It creates a user.
        """
        try:
            return UserService.create_user(username=username, email=email, password=password)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def create_superuser(username: str, email: str, password: str) -> User:
        """
        It creates a superuser.
        """
        try:
            return UserService.create_superuser(username=username, email=email, password=password)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_user_by_id(user_id: str) -> User:
        """
        It tries to get a user by id, and if it fails,
        it raises an HTTPException with the status code and message of the exception
        """
        try:
            return UserService.get_user_by_id(user_id=user_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_users() -> list:
        """
        It returns all users from the database
        """
        try:
            return UserService.get_all_users()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_active_users() -> list:
        """
        It returns all active users
        """
        try:
            return UserService.get_all_active_users()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def delete_user_by_id(user_id: str) -> JSONResponse:
        """
        This function deletes a user by id
        """
        try:
            UserService.delete(user_id=user_id)
            return JSONResponse(status_code=200, content=f"User with provided id {user_id} successfully deleted.")
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def update_user_active_status(user_id: str, active_status: bool) -> User:
        """
        It updates the active status of a user
        """
        try:
            return UserService.update_user_active_status(user_id=user_id, active_status=active_status)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def login_user(username_or_email: str, password: str) -> dict[str, str]:
        """
        It logs in a user as basic user or superuser
        """
        try:
            user = UserService.login_user(username_or_email=username_or_email, password=password)
            if user.superuser:
                return signJWT(user.id, "superuser")
            return signJWT(user.id, "user")
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
