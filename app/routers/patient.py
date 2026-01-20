# app/routers/patient.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.patient import PatientRegister, PatientUpdate, PatientOut
from app.schemas.user import UserOut

from app.services.patient_service import update_patient_profile, register_patient
from app.utils.role import role_required
from app.repositories import patient_repo

router = APIRouter(prefix="/patient", tags=["Patient"])


# View my patient profile
@router.get("/me", response_model=PatientOut)
def my_profile(db: Session = Depends(get_db), user = Depends(role_required("patient"))):
    return patient_repo.get_by_user(db, user.id)


# Update my patient profile
@router.put("/update", response_model=PatientOut)
def update_profile(update_data: PatientUpdate, db: Session = Depends(get_db), user = Depends(role_required("patient"))):
    return update_patient_profile(db, user.id, update_data.age, update_data.gender)

@router.post("/register/patient", response_model=UserOut)
def register_patient_endpoint(patient: PatientRegister, db: Session = Depends(get_db)):
    return register_patient(db, patient.name, patient.email, patient.password, patient.age, patient.gender)
