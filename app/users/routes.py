from fastapi import APIRouter

from app.users.controller import UserController
from app.users.schemas import UserSchemaIn, UserSchemaOut, UserSchemaLogin

user_router = APIRouter(prefix="/api/user", tags=["User"])


@user_router.post("/create-user", response_model=UserSchemaOut)
def create_user(user: UserSchemaIn):
    return UserController.create_user(username=user.username, email=user.email, password=user.password)


@user_router.post("/create-superuser", response_model=UserSchemaOut)
def create_superuser(user: UserSchemaIn):
    return UserController.create_superuser(username=user.username, email=user.email, password=user.password)


@user_router.get("/get-user-by-id/{user_id}", response_model=UserSchemaOut)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id=user_id)


@user_router.get("/get-all", response_model=list[UserSchemaOut])
def get_all_users():
    return UserController.get_all_users()


@user_router.delete("/delete-by-id", response_model=None)
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id=user_id)


@user_router.put("/update/active-status", response_model=UserSchemaOut)
def update_user_active_status(user_id: str, active_status: bool):
    return UserController.update_user_active_status(user_id=user_id, active_status=active_status)


@user_router.post("/login")
def login_user(user: UserSchemaLogin):
    return UserController.login_user(username_or_email=user.username_or_email, password=user.password)
