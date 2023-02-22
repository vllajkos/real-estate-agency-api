"""Follow controller layer"""
from fastapi import HTTPException
from starlette.responses import JSONResponse
from app.users.exceptions import CustomUserException
from app.users.models import Follow
from app.users.services import FollowService


class FollowController:
    """Class containing Follow controller methods"""
    @staticmethod
    def create(client_id: str, advertisement_id: str) -> Follow:
        """
        It creates a new follow relationship between a client and an advertisement
        """
        try:
            return FollowService.create(client_id=client_id, advertisement_id=advertisement_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_by_client_id(client_id: str) -> list:
        """
        It returns all follows of a client
        """
        try:
            return FollowService.get_all_by_client_id(client_id=client_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def get_all_by_advertisement_id(advertisement_id: str) -> list:
        """
        It returns all the followers of an advertisement
        """
        try:
            return FollowService.get_all_by_advertisement_id(advertisement_id=advertisement_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def get_by_client_id_and_advertisement_id(client_id: str, advertisement_id: str) -> Follow:
        """
        It gets a follow by client id and advertisement id
        """
        try:
            return FollowService.get_by_client_id_and_advertisement_id(client_id=client_id,
                                                                       advertisement_id=advertisement_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)

    @staticmethod
    def delete(client_id: str, advertisement_id: str) -> JSONResponse:
        """
        It deletes a follow relationship between a client and an advertisement.
        """
        try:
            FollowService.delete(client_id=client_id, advertisement_id=advertisement_id)
            return JSONResponse(status_code=200, content=f"Client id {client_id} unfollowed"
                                                         f" advertisement id {advertisement_id} ")
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
