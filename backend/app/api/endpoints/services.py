"""Service Endpoints"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.service import Service, ServiceCategory
from app.core.security import get_current_user
from app.core.exceptions import NotFoundException

router = APIRouter()

@router.get("/categories")
async def list_categories(db: Session = Depends(get_db)):
    """List all service categories"""
    categories = db.query(ServiceCategory).all()
    return categories

@router.get("/")
async def list_services(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    category_id: int = Query(None),
    technician_id: int = Query(None),
    db: Session = Depends(get_db)
):
    """List services"""
    query = db.query(Service).filter(Service.is_available == True)
    
    if category_id:
        query = query.filter(Service.category_id == category_id)
    if technician_id:
        query = query.filter(Service.technician_id == technician_id)
    
    services = query.offset(skip).limit(limit).all()
    return services

@router.get("/{service_id}")
async def get_service(service_id: int, db: Session = Depends(get_db)):
    """Get service by ID"""
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise NotFoundException("Service")
    return service
