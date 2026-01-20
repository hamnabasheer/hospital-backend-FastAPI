# app/schemas/patient.py

from pydantic import BaseModel, EmailStr

class PatientRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    age: int
    gender: str


class PatientOut(BaseModel):
    id: int
    age: int
    gender: str

    model_config = {
        "from_attributes": True
    }