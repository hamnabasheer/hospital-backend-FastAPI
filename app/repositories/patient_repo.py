# app/repositories/patient_repo.py

from sqlalchemy.orm import Session
from app.models.patient import Patient

def create(db: Session, patient: Patient):
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def get_by_user(db: Session, user_id: int):
    return db.query(Patient).filter(Patient.user_id == user_id).first()
