# app/schemas/doctor.py

from pydantic import BaseModel, EmailStr
from typing import Optional

class DoctorRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    specialization: str
    experience: int


class DoctorUpdate(BaseModel):
    specialization: Optional[str] = None
    experience: Optional[int] = None


class DoctorOut(BaseModel):
    id: int
    specialization: str
    experience: int
    approved: bool

    model_config = {
        "from_attributes": True
    }