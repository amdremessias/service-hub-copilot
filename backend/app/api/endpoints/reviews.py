"""Review Endpoints"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.review import Review
from app.core.security import get_current_user
from app.core.exceptions import NotFoundException

router = APIRouter()

@router.get("/technician/{technician_id}")
async def get_technician_reviews(
    technician_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get reviews for a technician"""
    reviews = db.query(Review).filter(Review.technician_id == technician_id).offset(skip).limit(limit).all()
    return reviews

@router.get("/{review_id}")
async def get_review(review_id: int, db: Session = Depends(get_db)):
    """Get review by ID"""
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise NotFoundException("Review")
    return review
