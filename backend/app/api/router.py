"""API Router Configuration"""
from fastapi import APIRouter
from app.api.endpoints import auth, users, technicians, services, bookings, reviews, payments, chat

api_router = APIRouter()

# Include routers
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(technicians.router, prefix="/technicians", tags=["Technicians"])
api_router.include_router(services.router, prefix="/services", tags=["Services"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["Bookings"])
api_router.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])
api_router.include_router(payments.router, prefix="/payments", tags=["Payments"])
api_router.include_router(chat.router, prefix="/chat", tags=["Chat"])
