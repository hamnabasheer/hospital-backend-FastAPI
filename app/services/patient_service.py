# app/services/patient_service.py

from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.repositories import patient_repo

def create_patient_profile(db: Session, user_id: int, age: int, gender: str):
    patient = Patient(
        user_id=user_id,
        age=age,
        gender=gender
    )
    return patient_repo.create(db, patient)
