# app/routers/admin.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.utils.role import role_required
from app.services.admin_service import approve_doctor
from app.repositories import doctor_repo, patient_repo

router = APIRouter(prefix="/admin", tags=["Admin"])


# View all doctors
@router.get("/doctors")
def all_doctors(db: Session = Depends(get_db), user = Depends(role_required("admin"))):
    return doctor_repo.get_all(db)


# Approve doctor
@router.put("/approve-doctor/{doctor_id}")
def approve(doctor_id: int, db: Session = Depends(get_db), user = Depends(role_required("admin"))):
    return approve_doctor(db, doctor_id)



@router.get("/patients")
def all_patients(db: Session = Depends(get_db), user = Depends(role_required("admin"))):
    return patient_repo.get_all(db)