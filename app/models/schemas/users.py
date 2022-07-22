from typing import Optional

from models.domain.users import User
from models.schemas.snschema import SNSchema
from pydantic import BaseModel, EmailStr, HttpUrl


class UserInLogin(SNSchema):
    email: EmailStr
    password: str


class UserInCreate(UserInLogin):
    first_name: str
    last_name: str
    username: str
    email: EmailStr


class UserInUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    image: Optional[HttpUrl] = None


class UserWithToken(User):
    token: str


class UserInResponse(SNSchema):
    user: UserWithToken
