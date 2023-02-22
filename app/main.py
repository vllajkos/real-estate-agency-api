"""Main app"""
import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.advertisements import advertisement_router
from app.db.database import Base, engine
from app.properties import (
    property_has_feature_router,
    property_router,
    type_of_feature_router,
    type_of_property_has_type_of_feature_router,
    type_of_property_router,
)
from app.users import client_router, employee_router, user_router
from app.users.routes import follow_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(type_of_property_router)
    app.include_router(type_of_feature_router)
    app.include_router(type_of_property_has_type_of_feature_router)
    app.include_router(property_router)
    app.include_router(property_has_feature_router)
    app.include_router(user_router)
    app.include_router(client_router)
    app.include_router(employee_router)
    app.include_router(advertisement_router)
    app.include_router(follow_router)
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
