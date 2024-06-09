from pydantic import BaseModel

class UserBase(BaseModel):
    fname: str
    email: str
    login: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
