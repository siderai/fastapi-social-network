from models.common import DateTimeModelMixin, IDModelMixin
from models.domain.base import SNModel
from models.domain.users import User


class Comment(IDModelMixin, DateTimeModelMixin, SNModel):
    body: str
    author: User
