from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.base import SNModel
from app.models.domain.users import User


class Message(IDModelMixin, DateTimeModelMixin, SNModel):
    from_: User
    to: User
    body: str
