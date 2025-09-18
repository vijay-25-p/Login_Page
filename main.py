from fastapi import FastAPI
from app import models, database
from app.routes import user_routes


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(user_routes.router, prefix="/user", tags=["Users"])
