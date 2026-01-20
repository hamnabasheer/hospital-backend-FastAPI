# app/schemas/patient.py

from pydantic import BaseModel, EmailStr
from typing import Optional

class PatientRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    age: int
    gender: str


class PatientUpdate(BaseModel):
    age: Optional[int] = None
    gender: Optional[str] = None


class PatientOut(BaseModel):
    age: int
    gender: str

    model_config = {
        "from_attributes": True
    }