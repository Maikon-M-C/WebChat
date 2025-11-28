from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserID(BaseModel):
    id: int


class UserPublic(UserID):
    username: str
    email: EmailStr


class PublicMessageSchema(BaseModel):
    user_id: int
    message: str