""" Routes for users, clients, employees and users following ads """
from fastapi import APIRouter
from app.users.controller import UserController, ClientController, EmployeeController, FollowController
from app.users.schemas import UserSchemaIn, UserSchemaOut, UserSchemaLogin, ClientSchemaOut, ClientSchemaIn, \
    EmployeeSchemaIn, EmployeeSchemaOut
from app.users.schemas import FollowSchema, FollowForClientSchema, FollowForAdSchema

user_router = APIRouter(prefix="/api/user", tags=["User"])


@user_router.post("/create-user", response_model=UserSchemaOut)
def create_user(user: UserSchemaIn):
    """
    Creates a basic user
    """
    return UserController.create_user(username=user.username, email=user.email, password=user.password)


@user_router.post("/create-superuser", response_model=UserSchemaOut)
def create_superuser(user: UserSchemaIn):
    """
    Creates superuser with privileges
    """
    return UserController.create_superuser(username=user.username, email=user.email, password=user.password)


@user_router.get("/get-user-by-id/{user_id}", response_model=UserSchemaOut)
def get_user_by_id(user_id: str):
    """
    Gets user by id
    """
    return UserController.get_user_by_id(user_id=user_id)


@user_router.get("/get-all", response_model=list[UserSchemaOut])
def get_all_users():
    """
    Gets all users
    """
    return UserController.get_all_users()


@user_router.get("/get-all-active", response_model=list[UserSchemaOut])
def get_all_active_users():
    """
    Gets all active users
    """
    return UserController.get_all_active_users()


@user_router.delete("/delete-by-id", response_model=None)
def delete_user_by_id(user_id: str):
    """
    Delete a user by id.
    """
    return UserController.delete_user_by_id(user_id=user_id)


@user_router.put("/update/active-status", response_model=UserSchemaOut)
def update_user_active_status(user_id: str, active_status: bool):
    """
    Update the active status of a user.
    """
    return UserController.update_user_active_status(user_id=user_id, active_status=active_status)


@user_router.post("/login")
def login_user(user: UserSchemaLogin):
    """
    Logs in user, returns token.
    """
    return UserController.login_user(username_or_email=user.username_or_email, password=user.password)


client_router = APIRouter(prefix="/api/client", tags=["Client"])


@client_router.post("/create-client", response_model=ClientSchemaOut)
def create_client(client: ClientSchemaIn):
    """
    Creates client
    """
    return ClientController.create_client(first_name=client.first_name, last_name=client.last_name,
                                          phone_number=client.phone_number, user_id=client.user_id)


@client_router.get("/get-all", response_model=list[ClientSchemaOut])
def get_all_clients():
    """
    This function returns a list of all clients
    """
    return ClientController.get_all_clients()


@client_router.get("/get-client-by-id/{client_id}", response_model=ClientSchemaOut)
def get_client_by_id(client_id: str):
    """
    Gets client by id
    """
    return ClientController.get_client_by_id(client_id=client_id)


@client_router.get("/get-client-by-user-id", response_model=ClientSchemaOut)
def get_client_by_user_id(user_id: str):
    """
    Gets client by user id
    """
    return ClientController.get_client_by_user_id(user_id=user_id)


@client_router.put("/update/phone-number", response_model=ClientSchemaOut)
def update_clients_phone_number(client_id: str, phone_number: str):
    """
    Update a client's phone number
    """
    return ClientController.update_clients_phone_number(client_id=client_id, phone_number=phone_number)


employee_router = APIRouter(prefix="/api/employee", tags=["Employee"])


@employee_router.post("/create-employee", response_model=EmployeeSchemaOut)
def create_employee(employee: EmployeeSchemaIn):
    """
    Creates an employee
    """
    return EmployeeController.create_employee(first_name=employee.first_name, last_name=employee.last_name,
                                              job_title=employee.job_title, phone_number=employee.phone_number,
                                              user_id=employee.user_id)


@employee_router.get("/get-all", response_model=list[EmployeeSchemaOut])
def get_all_employees():
    """
    This function returns all employees
    """
    return EmployeeController.get_all_employees()


@employee_router.get("/get-employee-by-id", response_model=EmployeeSchemaOut)
def get_employee_by_id(employee_id: str):
    """
    Gets employee by id
    """
    return EmployeeController.get_employee_by_id(employee_id=employee_id)


@employee_router.get("/get-employee-by-user-id", response_model=EmployeeSchemaOut)
def get_employee_by_user_id(user_id: str):
    """
    Gets employee by user id
    """
    return EmployeeController.get_employee_by_user_id(user_id=user_id)


@employee_router.put("/update/phone-number", response_model=EmployeeSchemaOut)
def update_employees_phone_number(employee_id: str, phone_number: str):
    """
    Update the phone number of an employee.
    """
    return EmployeeController.update_employee_phone_number(employee_id=employee_id, phone_number=phone_number)


@employee_router.put("/update/job_title", response_model=EmployeeSchemaOut)
def update_employees_job_title(employee_id: str, job_title: str):
    """
    Update the job title of an employee.
    """
    return EmployeeController.update_employee_job_title(employee_id=employee_id, job_title=job_title)


follow_router = APIRouter(prefix="/api/follow", tags=["Follow"])


@follow_router.post("/create-follow", response_model=FollowSchema)
def create_follow(follow: FollowSchema):
    """
    Create link between client and desired active advertisement
    """
    return FollowController.create(client_id=follow.client_id, advertisement_id=follow.advertisement_id)


@follow_router.get("/get-all-by-client-id", response_model=list[FollowForClientSchema])
def get_all_by_client_id(client_id: str):
    """
    Get all followed advertisements for client(by id)
    """
    return FollowController.get_all_by_client_id(client_id=client_id)


@follow_router.get("/get-all-by-advertisement-id", response_model=list[FollowForAdSchema])
def get_all_by_advertisement_id(advertisement_id: str):
    """
    Get all followers(clients) by advertisement id
    """
    return FollowController.get_all_by_advertisement_id(advertisement_id=advertisement_id)


@follow_router.get("/get-all-by-client-id-and-advertisement-id", response_model=FollowSchema)
def get_by_client_id_and_advertisement_id(client_id: str, advertisement_id: str):
    """
    Returns  follow object if client is following advertisement
    """
    return FollowController.get_by_client_id_and_advertisement_id(client_id=client_id,
                                                                  advertisement_id=advertisement_id)


@follow_router.delete("/unfollow", response_model=None)
def delete_follow(client_id: str, advertisement_id: str):
    """
    If client follows an ad, this route unfollows it
    """
    return FollowController.delete(client_id=client_id, advertisement_id=advertisement_id)
