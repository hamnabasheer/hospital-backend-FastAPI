# app/services/admin_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import doctor_repo

def approve_doctor(db: Session, doctor_id: int):
    doctor = doctor_repo.get_by_id(db, doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor.approved = True
    db.commit()
    db.refresh(doctor)

    return doctor
