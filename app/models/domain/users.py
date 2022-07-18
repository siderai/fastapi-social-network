import datetime
from typing import List, Optional

from app.models.common import IDModelMixin
from app.models.domain.base import SNModel
from app.services import security
from pydantic import EmailStr


class User(SNModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    signup_date: Optional[datetime.date]
    birthday: datetime.date
    image: Optional[str] = None
    friends: List[int] = []


class UserInDB(IDModelMixin, User):
    salt: str = ""
    hashed_password: str = ""

    def check_password(self, password: str) -> bool:
        return security.verify_password(self.salt + password, self.hashed_password)

    def change_password(self, password: str) -> None:
        self.salt = security.generate_salt()
        self.hashed_password = security.get_password_hash(self.salt + password)
