from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    db_user.id
    return db_user

async def signin_user(db: AsyncSession, email: str, password: str):
    result = await db.execute(
        select(models.User).where(
            models.User.email == email,
            models.User.password == password
        )
    )
    return result.scalars().first()
