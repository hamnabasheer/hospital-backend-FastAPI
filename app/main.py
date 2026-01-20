# app/main.py

from fastapi import FastAPI
from app.database import Base, engine

from app.routers import auth, doctor, patient, admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hospital Appointment & Medical Records API")

app.include_router(auth.router)
app.include_router(doctor.router)
app.include_router(patient.router)
app.include_router(admin.router)
