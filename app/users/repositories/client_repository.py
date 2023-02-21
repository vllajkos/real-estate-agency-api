from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import ClientIdDoesntExistException
from app.users.models import Client


class ClientRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_client(self, first_name: str, last_name: str, phone_number: str, user_id: str):
        try:
            client = Client(first_name=first_name, last_name=last_name, phone_number=phone_number, user_id=user_id)
            self.db.add(client)
            self.db.commit()
            self.db.refresh(client)
            return client
        except IntegrityError as err:
            raise err

    def get_client_by_user_id(self, user_id: str):
        return self.db.query(Client).filter(Client.user_id == user_id).first()

    # def get_by_name(self, first_name: str, last_name: str):
    #     return self.db.query(Client).filter((Client.first_name == first_name) & (Client.last_name == last_name)).all()
    #
    def get_client_by_id(self, client_id: str):
        return self.db.query(Client).filter(Client.id == client_id).first()

    #
    def get_all_clients(self):
        return self.db.query(Client).all()

    def delete(self, client_id: str):
        try:
            client = self.db.query(Client).filter(Client.id == client_id).first()
            if client:
                self.db.delete(client)
                self.db.commit()
                return
            raise ClientIdDoesntExistException
        except Exception as exc:
            raise exc

    def update_client_phone_number(self, client_id: str, phone_number: str):
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
