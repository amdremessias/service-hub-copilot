"""Authentication Endpoints"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, TokenResponse
from app.core.security import (
    hash_password, verify_password, create_access_token, create_refresh_token, get_current_user
)
from app.core.exceptions import ValidationException, UnauthorizedException

router = APIRouter()

@router.post("/register", response_model=TokenResponse)
async def register(user_create: UserCreate, db: Session = Depends(get_db)):
    """Register a new user"""
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user_create.email).first()
    if existing_user:
        raise ValidationException("Email already registered", "EMAIL_ALREADY_EXISTS")
    
    # Create new user
    new_user = User(
        email=user_create.email,
        password_hash=hash_password(user_create.password),
        first_name=user_create.first_name,
        last_name=user_create.last_name,
        role=user_create.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Generate tokens
    access_token = create_access_token({"sub": str(new_user.id)})
    refresh_token = create_refresh_token({"sub": str(new_user.id)})
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": 1800
    }

@router.post("/login", response_model=TokenResponse)
async def login(email: str, password: str, db: Session = Depends(get_db)):
    """Login user"""
    user = db.query(User).filter(User.email == email).first()
    
    if not user or not verify_password(password, user.password_hash):
        raise UnauthorizedException("Invalid credentials")
    
    if not user.is_active:
        raise UnauthorizedException("User is inactive")
    
    # Generate tokens
    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": 1800
    }

@router.get("/me")
async def get_current_user_info(current_user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get current user info"""
    user = db.query(User).filter(User.id == current_user_id).first()
    if not user:
        raise UnauthorizedException()
    return user
