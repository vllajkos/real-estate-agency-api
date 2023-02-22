"""Employee repository layer"""
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import EmployeeIdDoesntExistException
from app.users.models import Employee, User


class EmployeeRepository:
    """Class containing employee repository methods for retrieving data from database"""

    def __init__(self, db: Session) -> None:
        """Repository object"""
        self.db = db

    def create_employee(
        self, first_name: str, last_name: str, job_title: str, phone_number: str, user_id: str
    ) -> Employee:
        """
        It creates an employee object and adds it to the database
        """
        try:
            employee = Employee(
                first_name=first_name,
                last_name=last_name,
                job_title=job_title,
                phone_number=phone_number,
                user_id=user_id,
            )
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except IntegrityError as err:
            raise err

    def get_employee_by_user_id(self, user_id: str) -> Employee | None:
        """
        It returns the first employee that matches the user_id
        """
        return self.db.query(Employee).filter(Employee.user_id == user_id).first()

    def get_random_employee(self) -> Employee | None:
        """
        It returns a random employee from the database, but only if the employee is active
        """
        return self.db.query(Employee).join(User).filter(User.active_status == True).order_by(func.random()).first()

    def get_employee_by_id(self, employee_id: str) -> Employee | None:
        """
        It returns the first employee with the given id
        """
        return self.db.query(Employee).filter(Employee.id == employee_id).first()

    def get_all_employees(self) -> list:
        """
        It returns all the employees in the database
        """
        return self.db.query(Employee).all()

    def update_employee_phone_number(self, employee_id: str, phone_number: str) -> [Employee]:
        """
        It updates the phone number of an employee with the given employee id
        """
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            if employee:
                employee.phone_number = phone_number
                self.db.add(employee)
                self.db.commit()
                self.db.refresh(employee)
                return employee
            raise EmployeeIdDoesntExistException
        except Exception as exc:
            raise exc

    def update_employee_job_title(self, employee_id: str, job_title: str) -> [Employee]:
        """
        It updates the job title of an employee with the given employee id
        """
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            if employee:
                employee.job_title = job_title
                self.db.add(employee)
                self.db.commit()
                self.db.refresh(employee)
                return employee
            raise EmployeeIdDoesntExistException
        except Exception as exc:
            raise exc
