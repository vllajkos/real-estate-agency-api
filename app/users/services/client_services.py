"""Client service layer"""
from app.db.database import SessionLocal
from app.users.exceptions import (
    ClientDoesntExistForProvidedUserIdException,
    ClientExistWithProvidedUserIdException,
    ClientIdDoesntExistException,
)
from app.users.models import Client
from app.users.repositories import ClientRepository
from app.users.services import UserService


class ClientService:
    """Class containing client service layer methods"""

    @staticmethod
    def create_client(first_name: str, last_name: str, phone_number: str, user_id: str) -> Client:
        """
        It creates a client if the user exists and the client doesn't exist
        """
        with SessionLocal() as db:
            try:
                if UserService.get_user_by_id(user_id=user_id):
                    client_repository = ClientRepository(db)
                    if client_repository.get_client_by_user_id(user_id=user_id):
                        raise ClientExistWithProvidedUserIdException
                    return client_repository.create_client(
                        first_name=first_name, last_name=last_name, phone_number=phone_number, user_id=user_id
                    )
            except Exception as exc:
                raise exc

    @staticmethod
    def get_client_by_user_id(user_id: str) -> Client:
        """
        It gets a client by user id
        """
        with SessionLocal() as db:
            client_repository = ClientRepository(db)
            client = client_repository.get_client_by_user_id(user_id=user_id)
            if client:
                return client
            raise ClientDoesntExistForProvidedUserIdException

    @staticmethod
    def get_client_by_id(client_id: str) -> Client:
        """
        It gets a client by id
        """
        with SessionLocal() as db:
            client_repository = ClientRepository(db)
            client = client_repository.get_client_by_id(client_id=client_id)
            if client:
                return client
            raise ClientIdDoesntExistException

    @staticmethod
    def get_all_clients() -> list:
        """
        It gets all clients from the database
        """
        with SessionLocal() as db:
            client_repository = ClientRepository(db)
            return client_repository.get_all_clients()

    @staticmethod
    def update_client_phone_number(client_id: str, phone_number: str) -> Client:
        """
        It updates the phone number of a client with the given client id
        """
        with SessionLocal() as db:
            try:
                client_repository = ClientRepository(db)
                if client_repository.get_client_by_id(client_id=client_id):
                    return client_repository.update_client_phone_number(client_id=client_id, phone_number=phone_number)
                raise ClientIdDoesntExistException
            except Exception as exc:
                raise exc
