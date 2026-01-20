# app/services/doctor_service.py

from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.repositories import doctor_repo

def create_doctor_profile(db: Session, user_id: int, specialization: str, experience: int):
    doctor = Doctor(
        user_id=user_id,
        specialization=specialization,
        experience=experience,
        approved=False
    )
    return doctor_repo.create(db, doctor)
