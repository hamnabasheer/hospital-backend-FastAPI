# app/services/auth_service.py  

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories import user_repo
from app.models.user import User
from app.utils.security import hash_password, verify_password, create_access_token
from app.services.doctor_service import create_doctor_profile
from app.services.patient_service import create_patient_profile


def register_user(db: Session, name: str, email: str, password: str, role: str):
    if user_repo.get_by_email(db, email):
        raise HTTPException(status_code=400, detail="Email already exists")

    user = User(
        name=name,
        email=email,
        password=hash_password(password),
        role=role
    )

    user = user_repo.create(db, user)

    # 🔹 Auto create profile
    if role == "doctor":
        create_doctor_profile(db, user.id, "General", 0)

    if role == "patient":
        create_patient_profile(db, user.id, 0, "unknown")

    return user


def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token = create_access_token({
        "user_id": user.id,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user.role
    }