"""Employee controller layer"""
from fastapi import HTTPException
from starlette.responses import JSONResponse
from app.users.exceptions import CustomUserException
from app.users.models import Employee
from app.users.services import EmployeeService


class EmployeeController:
    """Class containing Employee controller methods"""

    @staticmethod
    def create_employee(first_name: str, last_name: str, job_title: str, phone_number: str, user_id: str) -> Employee:
        """
        It creates an employee
        """
        try:
            return EmployeeService.create_employee(first_name=first_name, last_name=last_name, job_title=job_title,
                                                   phone_number=phone_number, user_id=user_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_employee_by_user_id(user_id: str) -> Employee:
        """
        It gets an employee by user id
        """
        try:
            return EmployeeService.get_employee_by_user_id(user_id=user_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_employee_by_id(employee_id: str) -> Employee:
        """
        It gets an employee by id.
        """
        try:
            return EmployeeService.get_employee_by_id(employee_id=employee_id)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def get_all_employees() -> list:
        """
        It returns all employees from the database
        """
        try:
            return EmployeeService.get_all_employees()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def update_employee_phone_number(employee_id: str, phone_number: str) -> Employee:
        """
        It updates the phone number of an employee
        """
        try:
            return EmployeeService.update_employee_phone_number(employee_id=employee_id, phone_number=phone_number)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())

    @staticmethod
    def update_employee_job_title(employee_id: str, job_title: str) -> Employee:
        """
        It updates the job title of an employee.
        """
        try:
            return EmployeeService.update_employee_job_title(employee_id=employee_id, job_title=job_title)
        except CustomUserException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc.__str__())
