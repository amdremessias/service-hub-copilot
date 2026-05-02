"""Technician Model"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text, Table
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

# Association table for technician specializations
technician_specialization = Table(
    'technician_specialization',
    Base.metadata,
    Column('technician_id', Integer, ForeignKey('technicians.id'), primary_key=True),
    Column('specialization_id', Integer, ForeignKey('specializations.id'), primary_key=True)
)

class Technician(Base):
    __tablename__ = "technicians"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    company_name = Column(String(255), nullable=True)
    bio = Column(Text, nullable=True)
    years_of_experience = Column(Integer, default=0, nullable=False)
    rating = Column(Float, default=0.0, nullable=False)
    total_reviews = Column(Integer, default=0, nullable=False)
    hourly_rate = Column(Float, nullable=False)
    is_verified = Column(Integer, default=0, nullable=False)  # 0: unverified, 1: verified, 2: rejected
    document_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="technician")
    specializations = relationship(
        "Specialization",
        secondary=technician_specialization,
        back_populates="technicians"
    )
    services = relationship("Service", back_populates="technician")
    bookings = relationship("Booking", back_populates="technician", foreign_keys="Booking.technician_id")
    reviews = relationship("Review", back_populates="technician")
    chat_rooms = relationship("ChatRoom", back_populates="technician")
    
    def __repr__(self):
        return f"<Technician {self.user_id}>"

class Specialization(Base):
    __tablename__ = "specializations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    technicians = relationship(
        "Technician",
        secondary=technician_specialization,
        back_populates="specializations"
    )
    
    def __repr__(self):
        return f"<Specialization {self.name}>"
