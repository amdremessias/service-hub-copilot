"""Review Model"""
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class Review(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"), unique=True, nullable=False)
    reviewer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    technician_id = Column(Integer, ForeignKey("technicians.id"), nullable=False)
    rating = Column(Float, nullable=False)  # 1-5 stars
    comment = Column(Text, nullable=True)
    professionalism = Column(Float, nullable=True)  # 1-5
    punctuality = Column(Float, nullable=True)  # 1-5
    quality = Column(Float, nullable=True)  # 1-5
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    booking = relationship("Booking", back_populates="review")
    reviewer = relationship("User", back_populates="reviews")
    technician = relationship("Technician", back_populates="reviews")
    
    def __repr__(self):
        return f"<Review {self.id}>"
