# app/routers/patient.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.utils.role import role_required
from app.repositories import patient_repo

router = APIRouter(prefix="/patient", tags=["Patient"])


# View my patient profile
@router.get("/me")
def my_profile(db: Session = Depends(get_db), user = Depends(role_required("patient"))):
    return patient_repo.get_by_user(db, user.id)
