from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.base import SNModel
from app.models.domain.users import User
from pydantic import BaseModel


class TextModelMixin(BaseModel):
    body: str
    author: User


class Post(IDModelMixin, DateTimeModelMixin, TextModelMixin, SNModel):
    pass


class Like(SNModel):
    from_: User
    to: User
    subject: Post
