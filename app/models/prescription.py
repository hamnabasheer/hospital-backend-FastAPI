# app/models/prescription.py

from sqlalchemy import Column, Integer, ForeignKey, Text
from app.database import Base

class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    medicines = Column(Text)
    notes = Column(Text)
