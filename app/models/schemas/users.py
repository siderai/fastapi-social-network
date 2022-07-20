from typing import Optional

from app.models.domain.users import User
from app.models.schemas.snschema import SNSchema
from pydantic import BaseModel, EmailStr, HttpUrl


class UserInLogin(SNSchema):
    email: EmailStr
    password: str


class UserInCreate(UserInLogin):
    username: str
    email: EmailStr


class UserInUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[HttpUrl] = None


class UserWithToken(User):
    token: str


class UserInResponse(SNSchema):
    user: UserWithToken
