"""User Model"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum

from app.database import Base

class UserRole(str, Enum):
    CLIENT = "client"
    TECHNICIAN = "technician"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=True)
    profile_picture = Column(String(500), nullable=True)
    bio = Column(Text, nullable=True)
    role = Column(SQLEnum(UserRole), default=UserRole.CLIENT, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    technician = relationship("Technician", back_populates="user", uselist=False)
    bookings_as_client = relationship("Booking", back_populates="client", foreign_keys="Booking.client_id")
    reviews = relationship("Review", back_populates="reviewer")
    payments = relationship("Payment", back_populates="user")
    chat_rooms = relationship("ChatRoom", back_populates="client")
    
    def __repr__(self):
        return f"<User {self.email}>"
