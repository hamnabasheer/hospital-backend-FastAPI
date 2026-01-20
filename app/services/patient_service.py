# app/services/patient_service.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.models.user import User
from app.repositories import patient_repo, user_repo
from app.utils.security import hash_password

def create_patient_profile(db: Session, user_id: int, age: int, gender: str):
    patient = Patient(
        user_id=user_id,
        age=age,
        gender=gender
    )
    return patient_repo.create(db, patient)


def register_patient(db: Session, name: str, email: str, password: str, age: int, gender: str):
    if user_repo.get_by_email(db, email):
        raise HTTPException(status_code=400, detail="Email already exists")

    user = User(
        name=name,
        email=email,
        password=hash_password(password),
        role="patient"
    )

    user = user_repo.create(db, user)
    create_patient_profile(db, user.id, age, gender)

    return user


def update_patient_profile(db: Session, user_id: int, age: int = None, gender: str = None):
    patient = patient_repo.get_by_user(db, user_id)
    
    if not patient:
        raise HTTPException(status_code=404, detail="Patient profile not found")
    
    if age is not None:
        patient.age = age
    if gender is not None:
        patient.gender = gender
    
    return patient_repo.update(db, patient)