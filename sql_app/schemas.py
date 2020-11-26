from typing import Optional
from pydantic import BaseModel
import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str

class UserInDB(User):
    hashed_password: str

class UserCreate(User):
    password: str
    email: str

class PostBase(BaseModel):
    title:str
    body:str

class PostList(PostBase):
    created_date: Optional[datetime.datetime]
    owner_id: int
    owner: User

    class Config:
        orm_mode=True