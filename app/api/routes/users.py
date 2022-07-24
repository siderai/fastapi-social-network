from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter()


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


# created_at = Column(DateTime(), default=datetime.now)
# updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


Base.metadata.create_all(bind=engine)


from typing import List, Optional

from pydantic import EmailStr


class UserInResponce(BaseModel):
    id: int
    username: str
    password: str
    first_name: str
    last_name: str
    email: EmailStr


class UserInCreate(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: EmailStr


# users = {
#     {"id": 1, "username": "A"},
#     {"id": 2, "username": "B"},
#     {"id": 3, "username": "C"},
# }



# engine = create_engine("sqlite:///database.sqlite", echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()


@router.get("/users/{user_id}")
def retrieve_user(user_id: int) -> UserInResponce:
    return session.get(User, user_id)


@router.post("/users/")
def create_user(
    username: str, first_name: str, password: str, last_name: str, email: EmailStr
) -> UserInCreate:
    user = User(
        username=username,
        first_name=first_name,
        password=password,
        last_name=last_name,
        email=email,
    )
    print("USER", user)
    session.add(user)
    session.commit()
    return user


@router.get("/users/")
def retrieve_users():
    return session.query(User)


# from fastapi import APIRouter, Body, Depends, HTTPException
# from starlette.status import HTTP_400_BAD_REQUEST

# from api.dependencies.authentication import get_current_user_authorizer

# # from api.dependencies.database import get_repository
# from core.config import get_app_settings
# from core.settings.app import AppSettings
# from db.repositories.users import UsersRepository
# from models.domain.users import User
# from models.schemas.users import UserInResponse, UserInUpdate, UserWithToken
# from resources import strings
# from services import jwt
# from services.authentication import check_email_is_taken, check_username_is_taken

# router = APIRouter()


# @router.get("", response_model=UserInResponse, name="users:get-current-user")
# async def retrieve_current_user(
#     user: User = Depends(get_current_user_authorizer()),
#     settings: AppSettings = Depends(get_app_settings),
# ) -> UserInResponse:
#     token = jwt.create_access_token_for_user(
#         user,
#         str(settings.secret_key.get_secret_value()),
#     )
#     return UserInResponse(
#         user=UserWithToken(
#             username=user.username,
#             first_name=user.first_name,
#             last_name=user.last_name,
#             email=user.email,
#             signup_date=user.signup_date,
#             birthday=user.birthday,
#             image=user.image,
#             token=token,
#         ),
#     )


# @router.put("", response_model=UserInResponse, name="users:update-current-user")
# async def update_current_user(
#     user_update: UserInUpdate = Body(..., embed=True, alias="user"),
#     current_user: User = Depends(get_current_user_authorizer()),
#     # users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
#     settings: AppSettings = Depends(get_app_settings),
# # ) -> UserInResponse:
#     if user_update.username and user_update.username != current_user.username:
#         if await check_username_is_taken(users_repo, user_update.username):
#             raise HTTPException(
#                 status_code=HTTP_400_BAD_REQUEST,
#                 detail=strings.USERNAME_TAKEN,
#             )

#     if user_update.email and user_update.email != current_user.email:
#         if await check_email_is_taken(users_repo, user_update.email):
#             raise HTTPException(
#                 status_code=HTTP_400_BAD_REQUEST,
#                 detail=strings.EMAIL_TAKEN,
#             )

#     # user = await users_repo.update_user(user=current_user, **user_update.dict())

#     # token = jwt.create_access_token_for_user(
#     #     user,
#     #     str(settings.secret_key.get_secret_value()),
#     # )
#     # return UserInResponse(
#     #     user=UserWithToken(
#     #         username=user.username,
#     #         email=user.email,
#     #         bio=user.bio,
#     #         image=user.image,
#     #         # token=token,
#     #     ),
#     # )
