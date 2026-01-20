# app/models/doctor.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    specialization = Column(String)
    experience = Column(Integer)
    approved = Column(Boolean, default=False)
