# app/schemas/doctor.py

from pydantic import BaseModel, EmailStr

class DoctorRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    specialization: str
    experience: int


class DoctorOut(BaseModel):
    id: int
    specialization: str
    experience: int
    approved: bool

    model_config = {
        "from_attributes": True
    }