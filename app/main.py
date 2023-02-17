import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse


from app.db.database import engine, Base
from app.properties import type_of_property_router, type_of_feature_router, \
    type_of_property_has_type_of_feature_router, property_router, property_has_feature_router
from app.users import user_router, client_router, employee_router

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
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app)
