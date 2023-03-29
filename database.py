from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from settings import DB_PORT, DB_HOST, DB_PASSWORD, DB_USER, DB_NAME

engine = create_async_engine(f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db():
    try:
        session = async_session()
        yield session
    finally:
        await session.close()


Base = declarative_base()
