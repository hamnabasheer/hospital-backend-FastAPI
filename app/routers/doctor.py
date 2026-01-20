# app/routers/doctor.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.utils.role import role_required
from app.repositories import doctor_repo

router = APIRouter(prefix="/doctor", tags=["Doctor"])


# View my doctor profile
@router.get("/me")
def my_profile(db: Session = Depends(get_db), user = Depends(role_required("doctor"))):
    return doctor_repo.get_by_user(db, user.id)
