# app/models/appointment.py

from sqlalchemy import Column, Integer, ForeignKey, Date, Time, String
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    date = Column(Date)
    time = Column(Time)
    status = Column(String, default="pending")
