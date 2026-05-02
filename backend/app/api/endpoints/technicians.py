"""Technician Endpoints"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.technician import Technician, Specialization
from app.schemas.technician import TechnicianResponse, TechnicianCreate, TechnicianUpdate
from app.core.security import get_current_user
from app.core.exceptions import NotFoundException, ValidationException

router = APIRouter()

@router.post("/", response_model=TechnicianResponse)
async def create_technician(
    tech_create: TechnicianCreate,
    current_user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create technician profile"""
    # Check if technician already exists
    existing = db.query(Technician).filter(Technician.user_id == current_user_id).first()
    if existing:
        raise ValidationException("Technician profile already exists")
    
    technician = Technician(
        user_id=current_user_id,
        **tech_create.dict(exclude={"specialization_ids"})
    )
    
    if tech_create.specialization_ids:
        specs = db.query(Specialization).filter(Specialization.id.in_(tech_create.specialization_ids)).all()
        technician.specializations = specs
    
    db.add(technician)
    db.commit()
    db.refresh(technician)
    return technician

@router.get("/", response_model=List[TechnicianResponse])
async def list_technicians(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    specialization_id: int = Query(None),
    db: Session = Depends(get_db)
):
    """List all technicians"""
    query = db.query(Technician).filter(Technician.is_verified == 1)
    
    if specialization_id:
        query = query.filter(Technician.specializations.any(Specialization.id == specialization_id))
    
    technicians = query.offset(skip).limit(limit).all()
    return technicians

@router.get("/{technician_id}", response_model=TechnicianResponse)
async def get_technician(technician_id: int, db: Session = Depends(get_db)):
    """Get technician by ID"""
    technician = db.query(Technician).filter(Technician.id == technician_id).first()
    if not technician:
        raise NotFoundException("Technician")
    return technician

@router.put("/{technician_id}", response_model=TechnicianResponse)
async def update_technician(
    technician_id: int,
    tech_update: TechnicianUpdate,
    current_user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update technician profile"""
    technician = db.query(Technician).filter(Technician.id == technician_id).first()
    if not technician:
        raise NotFoundException("Technician")
    
    # Check ownership
    if technician.user_id != current_user_id:
        raise ValidationException("Unauthorized", "FORBIDDEN")
    
    # Update fields
    update_data = tech_update.dict(exclude_unset=True, exclude={"specialization_ids"})
    for field, value in update_data.items():
        setattr(technician, field, value)
    
    if tech_update.specialization_ids:
        specs = db.query(Specialization).filter(Specialization.id.in_(tech_update.specialization_ids)).all()
        technician.specializations = specs
    
    db.commit()
    db.refresh(technician)
    return technician
