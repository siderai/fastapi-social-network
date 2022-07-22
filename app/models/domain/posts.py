from models.common import DateTimeModelMixin, IDModelMixin
from models.domain.base import SNModel
from models.domain.users import User


class Post(IDModelMixin, DateTimeModelMixin, SNModel):
    body: str
    author: User


class Like(SNModel):
    from_: User
    to: User
    subject: Post
