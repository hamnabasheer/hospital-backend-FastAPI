# app/services/doctor_service.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.models.user import User
from app.repositories import doctor_repo, user_repo
from app.utils.security import hash_password

def create_doctor_profile(db: Session, user_id: int, specialization: str, experience: int):
    doctor = Doctor(
        user_id=user_id,
        specialization=specialization,
        experience=experience,
        approved=False
    )
    return doctor_repo.create(db, doctor)

def register_doctor(db: Session, name: str, email: str, password: str, specialization: str, experience: int):
    if user_repo.get_by_email(db, email):
        raise HTTPException(status_code=400, detail="Email already exists")

    user = User(
        name=name,
        email=email,
        password=hash_password(password),
        role="doctor"
    )

    user = user_repo.create(db, user)
    create_doctor_profile(db, user.id, specialization, experience)

    return user