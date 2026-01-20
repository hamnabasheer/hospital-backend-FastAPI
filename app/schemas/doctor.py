# app/schemas/doctor.py

from pydantic import BaseModel

class DoctorCreate(BaseModel):
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