# app/routers/auth.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordRequestForm

from app.database import get_db
from app.schemas.user import UserCreate, UserLogin, UserOut, LoginSchema
from app.services.auth_service import login_user
from app.schemas.doctor import DoctorRegister
from app.schemas.patient import PatientRegister

router = APIRouter(prefix="/auth", tags=["Authentication"])








@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    return login_user(db, form_data.username, form_data.password)

# @router.post("/login")
# def login(user: UserLogin, db: Session = Depends(get_db)):
#     token, db_user = login_user(db, user.email, user.password)
#     return token

#     return {
#         "access_token": token,
#         "token_type": "bearer",
#         "user": {
#             "id": db_user.id,
#             "name": db_user.name,
#             "role": db_user.role
#         }
#     }
