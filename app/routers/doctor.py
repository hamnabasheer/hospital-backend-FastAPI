# app/routers/doctor.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.doctor import DoctorRegister
from app.schemas.user import UserOut
from app.services.auth_service import register_doctor
from app.utils.role import role_required
from app.repositories import doctor_repo

router = APIRouter(prefix="/doctor", tags=["Doctor"])


@router.post("/register/doctor", response_model=UserOut)
def register_doctor_endpoint(doctor: DoctorRegister, db: Session = Depends(get_db)):
    return register_doctor(db, doctor.name, doctor.email, doctor.password, doctor.specialization, doctor.experience)

# View my doctor profile
@router.get("/me")
def my_profile(db: Session = Depends(get_db), user = Depends(role_required("doctor"))):
    return doctor_repo.get_by_user(db, user.id)
