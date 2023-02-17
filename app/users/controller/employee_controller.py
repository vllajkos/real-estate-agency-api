from fastapi import HTTPException
from starlette.responses import JSONResponse
from app.users.exceptions import CustomUserException
from app.users.services import EmployeeService, signJWT


class EmployeeController:
    @staticmethod
    def create_employee(first_name: str, last_name: str, job_title: str, phone_number: str, user_id: str):
        try:
            return EmployeeService.create_employee(first_name=first_name, last_name=last_name, job_title=job_title,
                                                   phone_number=phone_number, user_id=user_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
