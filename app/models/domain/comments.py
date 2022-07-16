from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.base import SNModel
from app.models.domain.users import User


class Comment(IDModelMixin, DateTimeModelMixin, SNModel):
    body: str
    author: User
