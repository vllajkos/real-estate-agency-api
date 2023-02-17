from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

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
