# app/routers/discovery.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.schemas.doctor import DoctorSearchResult
from app.repositories import doctor_repo
from app.models.user import User
from app.services import doctor_service

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/doctors", summary="Get all approved doctors", response_model=list[DoctorSearchResult])
def get_all_doctors(db: Session = Depends(get_db)):
    """Get list of all approved doctors"""
    return doctor_repo.get_all_approved(db)


# @router.get("/doctors/specialization/{specialization}", summary="Search doctors by specialization", response_model=list[DoctorSearchResult])
# def get_doctors_by_specialization(specialization: str, db: Session = Depends(get_db)):
#     """Get doctors by specialization (e.g., Cardiology, Neurology)"""
#     return doctor_repo.get_by_specialization(db, specialization)


@router.get("/doctors/search", summary="Search doctors by name and/or specialization", response_model=list[DoctorSearchResult])
def search_doctors(
    name: Optional[str] = None, 
    specialization: Optional[str] = None, 
    db: Session = Depends(get_db)
):
    
    return doctor_service.search_doctors(db, name, specialization)
