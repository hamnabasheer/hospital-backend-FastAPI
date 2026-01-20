# app/schemas/patient.py

from pydantic import BaseModel

class PatientCreate(BaseModel):
    age: int
    gender: str

class PatientOut(BaseModel):
    id: int
    age: int
    gender: str

    model_config = {
        "from_attributes": True
    }