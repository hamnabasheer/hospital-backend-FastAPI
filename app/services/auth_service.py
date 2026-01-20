# app/services/auth_service.py  

from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories import doctor_repo
from app.models.user import User
from app.utils.security import verify_password, create_access_token



def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    #  Check if doctor is approved
    if user.role == "doctor":
        doctor = doctor_repo.get_by_user(db, user.id)
        if not doctor or not doctor.approved:
            raise HTTPException(status_code=403, detail="Doctor not approved yet")

    token = create_access_token({
        "user_id": user.id,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user.role
    }