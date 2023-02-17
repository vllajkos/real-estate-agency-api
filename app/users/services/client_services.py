import hashlib
from app.db.database import SessionLocal
from app.users.exceptions import ClientExistWithProvidedUserIdException
# from app.clients.exceptions import InvalidClientnameException, InvalidEmailException, ClientIdDoesntExistException, \
#     InvalidPasswordException, InvalidLoginInfoException

from app.users.repositories import ClientRepository

from app.users.services import UserService


class ClientService:
    @staticmethod
    def create_client(first_name: str, last_name: str, phone_number: str, user_id: str):
        with SessionLocal() as db:
            try:
                if UserService.get_user_by_id(user_id=user_id):
                    client_repository = ClientRepository(db)
                    if client_repository.get_client_by_user_id(user_id=user_id):
                        raise ClientExistWithProvidedUserIdException
                    return client_repository.create_client(first_name=first_name,
                                                           last_name=last_name,
                                                           phone_number=phone_number, user_id=user_id)
            except Exception as exc:
                raise exc

    # @staticmethod
    # def create_superclient(first_name: str, last_name: str, phone_number: str):
    #     with SessionLocal() as db:
    #         try:
    #             client_repository = ClientRepository(db)
    #             if client_repository.get_by_first_name(first_name=first_name):
    #                 raise InvalidClientnameException
    #             if client_repository.get_by_last_name(last_name=last_name):
    #                 raise InvalidEmailException
    #             hashed_phone_number = hashlib.sha256(bytes(phone_number, "utf-8")).hexdigest()
    #             return client_repository.create_superclient(first_name=first_name, last_name=last_name, phone_number=hashed_phone_number)
    #         except Exception as exc:
    #             raise exc
    #
    # @staticmethod
    # def get_client_by_id(client_id: str):
    #     with SessionLocal() as db:
    #         client_repository = ClientRepository(db)
    #         client = client_repository.get_client_by_id(client_id=client_id)
    #         if client:
    #             return client
    #         raise ClientIdDoesntExistException
    #
    # @staticmethod
    # def get_all_clients():
    #     with SessionLocal() as db:
    #         client_repository = ClientRepository(db)
    #         return client_repository.get_all_clients()
    #
    # @staticmethod
    # def delete(client_id: str):
    #     try:
    #         with SessionLocal() as db:
    #             client_repository = ClientRepository(db)
    #             if client_repository.get_client_by_id(client_id=client_id):
    #                 return client_repository.delete(client_id)
    #             raise ClientIdDoesntExistException
    #     except Exception as exc:
    #         raise exc
    #
    # @staticmethod
    # def update_client_active_status(client_id: str, active_status: bool):
    #     with SessionLocal() as db:
    #         try:
    #             client_repository = ClientRepository(db)
    #             if client_repository.get_client_by_id(client_id=client_id):
    #                 return client_repository.update_client_active_status(client_id=client_id, active_status=active_status)
    #             raise ClientIdDoesntExistException
    #         except Exception as exc:
    #             raise exc
    #
    # @staticmethod
    # def login_client(first_name_or_last_name: str, phone_number: str):
    #     with SessionLocal() as db:
    #         try:
    #             client_repository = ClientRepository(db)
    #             client = client_repository.get_by_first_name_or_last_name(first_name_or_last_name=first_name_or_last_name)
    #             if client:
    #                 if hashlib.sha256(bytes(phone_number, "utf-8")).hexdigest() == client.phone_number:
    #                     return client
    #                 raise InvalidPasswordException
    #             raise InvalidLoginInfoException
    #         except Exception as exc:
    #             raise exc
