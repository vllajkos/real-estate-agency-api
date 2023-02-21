from app.db.database import SessionLocal
from app.users.exceptions import EmployeeExistWithProvidedUserIdException, NoEmployeesYetException, \
    EmployeeDoesntExistforProvidedUserIdException, EmployeeIdDoesntExistException


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

    @staticmethod
    def get_employee_by_user_id(user_id: str):
        with SessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee = employee_repository.get_employee_by_user_id(user_id=user_id)
            if employee:
                return employee
            raise EmployeeDoesntExistforProvidedUserIdException

    @staticmethod
    def get_employee_by_id(employee_id: str):
        with SessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            employee = employee_repository.get_employee_by_id(employee_id=employee_id)
            if employee:
                return employee
            raise EmployeeIdDoesntExistException

    @staticmethod
    def get_all_employees():
        with SessionLocal() as db:
            employee_repository = EmployeeRepository(db)
            return employee_repository.get_all_employees()

    @staticmethod
    def delete(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                if employee_repository.get_employee_by_id(employee_id=employee_id):
                    return employee_repository.delete(employee_id)
                raise EmployeeIdDoesntExistException
        except Exception as exc:
            raise exc

    @staticmethod
    def update_employee_phone_number(employee_id: str, phone_number: str):
        with SessionLocal() as db:
            try:
                employee_repository = EmployeeRepository(db)
                if employee_repository.get_employee_by_id(employee_id=employee_id):
                    return employee_repository.update_employee_phone_number(employee_id=employee_id,
                                                                            phone_number=phone_number)
                raise EmployeeIdDoesntExistException
            except Exception as exc:
                raise exc

    @staticmethod
    def update_employee_job_title(employee_id: str, job_title: str):
        with SessionLocal() as db:
            try:
                employee_repository = EmployeeRepository(db)
                if employee_repository.get_employee_by_id(employee_id=employee_id):
                    return employee_repository.update_employee_job_title(employee_id=employee_id,
                                                                         job_title=job_title)
                raise EmployeeIdDoesntExistException
            except Exception as exc:
                raise exc
