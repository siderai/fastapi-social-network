from models.common import DateTimeModelMixin, IDModelMixin
from models.domain.base import SNModel
from models.domain.users import User


class Message(IDModelMixin, DateTimeModelMixin, SNModel):
    from_: User
    to: User
    body: str
