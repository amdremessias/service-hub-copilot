"""Booking Schemas"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    NO_SHOW = "no_show"

class BookingCreate(BaseModel):
    service_id: int
    technician_id: int
    scheduled_date: datetime
    duration_minutes: int = Field(gt=0)
    address: str = Field(min_length=5)
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    notes: Optional[str] = None

class BookingUpdate(BaseModel):
    scheduled_date: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    address: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[BookingStatus] = None

class BookingResponse(BaseModel):
    id: int
    client_id: int
    technician_id: int
    service_id: int
    scheduled_date: datetime
    duration_minutes: int
    address: str
    notes: Optional[str]
    status: BookingStatus
    latitude: Optional[str]
    longitude: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
