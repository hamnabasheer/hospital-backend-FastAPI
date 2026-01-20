# app/repositories/doctor_repo.py

from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.models.user import User

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

def get_all_approved(db: Session):
    doctors = db.query(Doctor).join(User).filter(Doctor.approved == True).all()
    for doctor in doctors:
        user = db.query(User).filter(User.id == doctor.user_id).first()
        doctor.name = user.name if user else "Unknown"
    return doctors

# def get_by_specialization(db: Session, specialization: str):
#     doctors = db.query(Doctor).join(User).filter(
#         Doctor.approved == True,
#         Doctor.specialization.ilike(f"%{specialization}%")
#     ).all()
#     for doctor in doctors:
#         user = db.query(User).filter(User.id == doctor.user_id).first()
#         doctor.name = user.name if user else "Unknown"
#     return doctors

def search_doctors(db: Session, name: str = None, specialization: str = None):
    query = db.query(Doctor).filter(Doctor.approved == True)
    
    if name:
        query = query.join(User).filter(User.name.ilike(f"%{name}%"))
    else:
        query = query.join(User)
    
    if specialization:
        query = query.filter(Doctor.specialization.ilike(f"%{specialization}%"))
    
    doctors = query.all()
    for doctor in doctors:
        user = db.query(User).filter(User.id == doctor.user_id).first()
        doctor.name = user.name if user else "Unknown"
    return doctors
