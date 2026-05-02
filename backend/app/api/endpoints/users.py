"""User Endpoints"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate
from app.core.security import get_current_user
from app.core.exceptions import NotFoundException

router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get current user"""
    user = db.query(User).filter(User.id == current_user_id).first()
    if not user:
        raise NotFoundException("User")
    return user

@router.put("/me", response_model=UserResponse)
async def update_current_user(
    user_update: UserUpdate,
    current_user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update current user"""
    user = db.query(User).filter(User.id == current_user_id).first()
    if not user:
        raise NotFoundException("User")
    
    # Update fields
    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)
    
    db.commit()
    db.refresh(user)
    return user

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get user by ID"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise NotFoundException("User")
    return user
