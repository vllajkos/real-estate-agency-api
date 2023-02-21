from fastapi import HTTPException
from starlette.responses import JSONResponse
from app.users.exceptions import CustomUserException
from app.users.services import ClientService, signJWT


class ClientController:
    @staticmethod
    def create_client(first_name: str, last_name: str, phone_number: str, user_id: str):
        try:
            return ClientService.create_client(first_name=first_name, last_name=last_name, phone_number=phone_number,
                                               user_id=user_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    #
    # @staticmethod
    # def create_superuser(username: str, email: str, password: str):
    #     try:
    #         return UserService.create_superuser(username=username, email=email, password=password)
    #     except CustomUserException as exc:
    #         raise HTTPException(status_code=exc.status_code, detail=exc.message)
    #     except Exception as exc:
    #         raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_client_by_user_id(user_id: str):
        try:
            return ClientService.get_client_by_user_id(user_id=user_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
    @staticmethod
    def get_client_by_id(client_id: str):
        try:
            return ClientService.get_client_by_id(client_id=client_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_clients():
        try:
            return ClientService.get_all_clients()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def delete_client_by_id(client_id: str):
        try:
            ClientService.delete(client_id=client_id)
            return JSONResponse(status_code=200, content=f"Client with provided id {client_id} successfully deleted.")
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def update_clients_phone_number(client_id: str, phone_number: str):
        try:
            return ClientService.update_client_phone_number(client_id=client_id, phone_number=phone_number)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    # @staticmethod
    # def login_user(username_or_email: str, password: str):
    #     try:
    #         user = UserService.login_user(username_or_email=username_or_email, password=password)
    #         if user.superuser:
    #             return signJWT(user.id, "superuser")
    #         return signJWT(user.id, "user")
    #     except CustomUserException as exc:
    #         raise HTTPException(status_code=exc.status_code, detail=exc.message)
    #     except Exception as exc:
    #         raise HTTPException(status_code=500, detail=exc.__str__())
