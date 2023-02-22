"""Client controller layer"""
from fastapi import HTTPException
from starlette.responses import JSONResponse

from app.users.exceptions import CustomUserException
from app.users.models import Client
from app.users.services import ClientService


class ClientController:
    """Class containing client controller methods"""

    @staticmethod
    def create_client(first_name: str, last_name: str, phone_number: str, user_id: str) -> Client:
        """
        It creates a client
        """
        try:
            return ClientService.create_client(
                first_name=first_name, last_name=last_name, phone_number=phone_number, user_id=user_id
            )
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_client_by_user_id(user_id: str) -> Client:
        """
        It gets a client by user id
        """
        try:
            return ClientService.get_client_by_user_id(user_id=user_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_client_by_id(client_id: str) -> Client:
        """
        It gets a client by id
        """
        try:
            return ClientService.get_client_by_id(client_id=client_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_clients() -> list:
        """
        It returns all clients from the database
        """
        try:
            return ClientService.get_all_clients()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def update_clients_phone_number(client_id: str, phone_number: str) -> Client:
        """
        It updates the phone number of a client
        """
        try:
            return ClientService.update_client_phone_number(client_id=client_id, phone_number=phone_number)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
