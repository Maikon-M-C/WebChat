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

class MessageSchema(BaseModel):
    username: str
    message: str

class PublicMessageSchema(BaseModel):
    username: str
    message: str

class PrivateMessageSchema(BaseModel):
    username: str
    message: str
    from_username: str