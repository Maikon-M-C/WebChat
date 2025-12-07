from pydantic import BaseModel, EmailStr
from typing import List


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPublic(BaseModel):
    username: str
    email: EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ListUsersSchema(BaseModel):
    users: List[UserPublic]


class PublicMessageSchema(BaseModel):
    user_id: int
    message: str