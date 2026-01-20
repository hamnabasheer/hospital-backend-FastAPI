# app/main.py

from fastapi import FastAPI
from app.database import Base, engine

from app.routers import auth, doctor, patient, admin, discovery

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hospital API")

app.include_router(auth.router)
app.include_router(doctor.router)
app.include_router(patient.router)
app.include_router(admin.router)
app.include_router(discovery.router)
