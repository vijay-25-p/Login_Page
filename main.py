from fastapi import FastAPI
from app import models, database
from app.routes import user_routes

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


app.include_router(user_routes.router, prefix="/user", tags=["Users"])
 