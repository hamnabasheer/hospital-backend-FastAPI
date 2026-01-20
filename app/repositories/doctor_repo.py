# app/repositories/doctor_repo.py

from sqlalchemy.orm import Session
from app.models.doctor import Doctor

def create(db: Session, doctor: Doctor):
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

def get_by_user(db: Session, user_id: int):
    return db.query(Doctor).filter(Doctor.user_id == user_id).first()

def get_all(db: Session):
    return db.query(Doctor).all()

def get_by_id(db: Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def update(db: Session, doctor: Doctor):
    db.commit()
    db.refresh(doctor)
    return doctor
