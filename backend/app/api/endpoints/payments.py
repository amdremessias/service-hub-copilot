"""Payment Endpoints"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.payment import Payment
from app.core.security import get_current_user
from app.core.exceptions import NotFoundException

router = APIRouter()

@router.get("/")
async def list_payments(
    current_user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List user payments"""
    payments = db.query(Payment).filter(Payment.user_id == current_user_id).all()
    return payments

@router.get("/{payment_id}")
async def get_payment(
    payment_id: int,
    current_user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get payment by ID"""
    payment = db.query(Payment).filter(Payment.id == payment_id, Payment.user_id == current_user_id).first()
    if not payment:
        raise NotFoundException("Payment")
    return payment
