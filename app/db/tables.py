from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/asyncalchemy"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = AsyncSession(engine, expire_on_commit=False)

Base = declarative_base()

# async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# async def get_session() -> AsyncSession:
#     async with async_session() as session:
#         yield session


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), nullable=False, index=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    image = Column(String(255))
    # friends = relationship("User", back_populates="Friend")
    country = Column(String(80))
    city = Column(String(50))

    def __repr__(self):
        return f"User(id={self.id!r}, \
                      username={self.username!r}, \
                      fullname={self.first_name!r} {self.last_name!r}, \
                      email={self.email!r})"


async def main():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
