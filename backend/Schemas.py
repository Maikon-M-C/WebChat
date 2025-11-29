from pydantic import BaseModel, EmailStr
from typing import List


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserID(BaseModel):
    id: int


class UserPublic(UserID):
    username: str
    email: EmailStr


class ListUsersSchema(BaseModel):
    users: List[UserPublic]


class PublicMessageSchema(BaseModel):
    user_id: int
    message: str