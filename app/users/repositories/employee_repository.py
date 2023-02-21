from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import EmployeeIdDoesntExistException
# from app.users.exceptions import EmployeeIdDoesntExistException
from app.users.models import Employee


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, first_name: str, last_name: str, job_title: str, phone_number: str, user_id: str):
        try:
            employee = Employee(first_name=first_name, last_name=last_name, job_title=job_title,
                                phone_number=phone_number, user_id=user_id)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except IntegrityError as err:
            raise err

    def get_employee_by_user_id(self, user_id: str):
        return self.db.query(Employee).filter(Employee.user_id == user_id).first()

    def get_random_employee(self):
        return self.db.query(Employee).order_by(func.random()).first()

    def get_employee_by_id(self, employee_id: str):
        return self.db.query(Employee).filter(Employee.id == employee_id).first()

    def get_all_employees(self):
        return self.db.query(Employee).all()

    def delete(self, employee_id: str):
        try:
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            if employee:
                self.db.delete(employee)
                self.db.commit()
                return
            raise EmployeeIdDoesntExistException
        except Exception as exc:
            raise exc

    def update_employee_phone_number(self, employee_id: str, phone_number: str):
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

    def update_employee_job_title(self, employee_id: str, job_title: str):
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
