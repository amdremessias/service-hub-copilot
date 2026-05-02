"""Technician Schemas"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class SpecializationBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: Optional[str] = None

class SpecializationResponse(SpecializationBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class TechnicianCreate(BaseModel):
    company_name: Optional[str] = None
    bio: Optional[str] = None
    years_of_experience: int = Field(ge=0)
    hourly_rate: float = Field(gt=0)
    specialization_ids: List[int] = Field(default_factory=list)

class TechnicianUpdate(BaseModel):
    company_name: Optional[str] = None
    bio: Optional[str] = None
    years_of_experience: Optional[int] = None
    hourly_rate: Optional[float] = None
    specialization_ids: Optional[List[int]] = None

class TechnicianResponse(BaseModel):
    id: int
    user_id: int
    company_name: Optional[str]
    bio: Optional[str]
    years_of_experience: int
    rating: float
    total_reviews: int
    hourly_rate: float
    is_verified: int
    specializations: List[SpecializationResponse]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
