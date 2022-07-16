from datetime import date
from typing import List, Optional

from app.models.common import IDModelMixin
from app.models.domain.base import SNModel


class User(IDModelMixin, SNModel):
    username: str
    first_name: str
    last_name: str
    signup_date: Optional[date]
    birthday: Optional[date]
    image: Optional[str] = None
    friends: List[int] = []
