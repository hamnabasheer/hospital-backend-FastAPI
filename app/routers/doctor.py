# app/routers/doctor.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.doctor import DoctorRegister, DoctorUpdate, DoctorOut
from app.schemas.user import UserOut
 
from app.services.doctor_service import update_doctor_profile, register_doctor
from app.utils.role import role_required
from app.repositories import doctor_repo

router = APIRouter(prefix="/doctor", tags=["Doctor"])


@router.post("/register/doctor", summary="Register a new doctor", response_model=UserOut)
def register_doctor_endpoint(doctor: DoctorRegister, db: Session = Depends(get_db)):
    return register_doctor(db, doctor.name, doctor.email, doctor.password, doctor.specialization, doctor.experience)

#view doctor's profile
@router.get("/me", summary="view doctor profile", response_model=DoctorOut)
def my_profile(db: Session = Depends(get_db), user = Depends(role_required("doctor"))):
    return doctor_repo.get_by_user(db, user.id)


# Update my doctor profile
@router.put("/update", summary="update doctor profile", response_model=DoctorOut)
def update_profile(update_data: DoctorUpdate, db: Session = Depends(get_db), user = Depends(role_required("doctor"))):
    return update_doctor_profile(db, user.id, update_data.specialization, update_data.experience)
