import hashlib
from app.db.database import SessionLocal
from app.users.exceptions import EmployeeExistWithProvidedUserIdException, NoEmployeesYetException
# from app.employees.exceptions import InvalidEmployeenameException, InvalidEmailException, EmployeeIdDoesntExistException, \
#     InvalidPasswordException, InvalidLoginInfoException

from app.users.repositories import EmployeeRepository

from app.users.services import UserService


class EmployeeService:
    @staticmethod
    def create_employee(first_name: str, last_name: str, job_title: str, phone_number: str, user_id: str):
        try:
            with SessionLocal() as db:
                if UserService.get_user_by_id(user_id=user_id):
                    employee_repository = EmployeeRepository(db)
                    if employee_repository.get_employee_by_user_id(user_id=user_id):
                        raise EmployeeExistWithProvidedUserIdException
                    return employee_repository.create_employee(first_name=first_name, last_name=last_name,
                                                               job_title=job_title, phone_number=phone_number,
                                                               user_id=user_id)
        except Exception as exc:
            raise exc

    @staticmethod
    def get_random_employee():
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                employee = employee_repository.get_random_employee()
                if employee:
                    return employee
                raise NoEmployeesYetException
        except Exception as exc:
            raise exc
