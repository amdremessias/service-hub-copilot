"""Booking Endpoints"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.booking import Booking
from app.schemas.booking import BookingCreate, BookingResponse, BookingUpdate
from app.core.security import get_current_user
from app.core.exceptions import NotFoundException

router = APIRouter()

@router.post("/", response_model=BookingResponse)
async def create_booking(
    booking_create: BookingCreate,
    current_user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new booking"""
    booking = Booking(
        client_id=current_user_id,
        **booking_create.dict()
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

@router.get("/my-bookings", response_model=List[BookingResponse])
async def get_my_bookings(
    current_user_id: int = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get current user's bookings"""
    bookings = db.query(Booking).filter(Booking.client_id == current_user_id).offset(skip).limit(limit).all()
    return bookings

@router.get("/{booking_id}", response_model=BookingResponse)
async def get_booking(booking_id: int, db: Session = Depends(get_db)):
    """Get booking by ID"""
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise NotFoundException("Booking")
    return booking

@router.put("/{booking_id}", response_model=BookingResponse)
async def update_booking(
    booking_id: int,
    booking_update: BookingUpdate,
    current_user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update booking"""
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise NotFoundException("Booking")
    
    # Check ownership
    if booking.client_id != current_user_id:
        raise NotFoundException("Booking")
    
    update_data = booking_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(booking, field, value)
    
    db.commit()
    db.refresh(booking)
    return booking
