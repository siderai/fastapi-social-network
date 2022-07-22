from fastapi import APIRouter, Body

from pydantic import BaseModel

router = APIRouter()


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///database.sqlite", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), nullable=False, index=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, index=True)
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


# created_at = Column(DateTime(), default=datetime.now)
# updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


Base.metadata.create_all(bind=engine)


from typing import List, Optional
from pydantic import EmailStr


class UserInResponce(BaseModel):
    id: int
    username: str
    password: str
    first_name: str
    last_name: str
    email: EmailStr


class UserInCreate(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: EmailStr


# users = {
#     {"id": 1, "username": "A"},
#     {"id": 2, "username": "B"},
#     {"id": 3, "username": "C"},
# }


@router.get("/users/{user_id}")
def retrieve_user(user_id: int) -> UserInResponce:
    return session.get(User, user_id)


@router.post("/users/")
def create_user(
    username: str, first_name: str, password: str, last_name: str, email: EmailStr
) -> UserInCreate:
    user = User(
        username=username,
        first_name=first_name,
        password=password,
        last_name=last_name,
        email=email,
    )
    print("USER", user)
    session.add(user)
    session.commit()
    return user


@router.get("/users/")
def retrieve_users():
    return session.query(User)
