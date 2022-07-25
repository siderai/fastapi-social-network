# from app.models.schemas.users import UserInCreate, UserInResponse, UserInUpdate


from sqlalchemy.ext.asyncio import AsyncSession

from app.models.domain.users import UserInDB
from app.models.orm.models import User


async def create_user(
    session: AsyncSession,
    username: str,
    email: str,
    password: str,
) -> UserInDB:
    user = User(username=username, email=email)
    session.add(User)
    await session.commit()

    return user


# hash pw


# async def update_user():
#     pass
