# app/schemas/user.py

from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str   # patient / doctor


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class LoginSchema(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    role: str

    model_config = {
        "from_attributes": True
    }
