# app/routers/patient.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.patient import PatientRegister
from app.schemas.user import UserOut
from app.services.auth_service import register_patient
from app.utils.role import role_required
from app.repositories import patient_repo

router = APIRouter(prefix="/patient", tags=["Patient"])


# View my patient profile
@router.get("/me")
def my_profile(db: Session = Depends(get_db), user = Depends(role_required("patient"))):
    return patient_repo.get_by_user(db, user.id)

@router.post("/register/patient", response_model=UserOut)
def register_patient_endpoint(patient: PatientRegister, db: Session = Depends(get_db)):
    return register_patient(db, patient.name, patient.email, patient.password, patient.age, patient.gender)
