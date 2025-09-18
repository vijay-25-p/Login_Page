from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL,
                             pool_size=25,
                             max_overflow=65,
                             pool_recycle=1800,
                             echo=False)
AsyncSessionLocal = async_sessionmaker(expire_on_commit=False, bind=engine)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
    
