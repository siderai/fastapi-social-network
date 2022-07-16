from datetime import date
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    signup_date: Optional[date]
    birthday: Optional[date]
    friends: List[int] = []


class Post(BaseModel):
    pass


class Like(BaseModel):
    pass


class Message(BaseModel):
    pass


class Comment(BaseModel):
    pass
