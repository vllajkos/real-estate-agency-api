"""Client repository layer"""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import ClientIdDoesntExistException
from app.users.models import Client


class ClientRepository:
    """Class containing client repository methods for retrieving data from database"""

    def __init__(self, db: Session) -> None:
        """Creating object of client repository class"""
        self.db = db

    def create_client(self, first_name: str, last_name: str, phone_number: str, user_id: str) -> Client:
        """
        It creates a new client in the database
        """
        try:
            client = Client(first_name=first_name, last_name=last_name, phone_number=phone_number, user_id=user_id)
            self.db.add(client)
            self.db.commit()
            self.db.refresh(client)
            return client
        except IntegrityError as err:
            raise err

    def get_client_by_user_id(self, user_id: str) -> Client | None:
        """
        It returns the first client object that matches the user_id passed in as a parameter
        """
        return self.db.query(Client).filter(Client.user_id == user_id).first()

    def get_client_by_id(self, client_id: str) -> Client | None:
        """
        This function returns the first client in the database with the given client_id
        """
        return self.db.query(Client).filter(Client.id == client_id).first()

    #
    def get_all_clients(self) -> list:
        """
        It returns all the clients in the database
        """
        return self.db.query(Client).all()

    def update_client_phone_number(self, client_id: str, phone_number: str) -> [Client]:
        """
        It updates the phone number of a client in the database
        """
        try:
            client = self.db.query(Client).filter(Client.id == client_id).first()
            if client:
                client.phone_number = phone_number
                self.db.add(client)
                self.db.commit()
                self.db.refresh(client)
                return client
            raise ClientIdDoesntExistException
        except Exception as exc:
            raise exc
