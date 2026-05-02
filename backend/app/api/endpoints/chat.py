"""Chat Endpoints"""
from fastapi import APIRouter, Depends, Query, WebSocket
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.chat import ChatRoom, ChatMessage
from app.core.security import get_current_user
from app.core.exceptions import NotFoundException

router = APIRouter()

@router.get("/rooms")
async def list_chat_rooms(
    current_user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List user chat rooms"""
    rooms = db.query(ChatRoom).filter(
        (ChatRoom.client_id == current_user_id) | (ChatRoom.technician_id == current_user_id)
    ).all()
    return rooms

@router.get("/rooms/{room_id}")
async def get_chat_room(
    room_id: int,
    current_user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get chat room messages"""
    room = db.query(ChatRoom).filter(ChatRoom.id == room_id).first()
    if not room:
        raise NotFoundException("Chat Room")
    
    # Check access
    if room.client_id != current_user_id and room.technician_id != current_user_id:
        raise NotFoundException("Chat Room")
    
    return room

@router.get("/rooms/{room_id}/messages")
async def get_chat_messages(
    room_id: int,
    current_user_id: int = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get chat messages from a room"""
    room = db.query(ChatRoom).filter(ChatRoom.id == room_id).first()
    if not room:
        raise NotFoundException("Chat Room")
    
    messages = db.query(ChatMessage).filter(ChatMessage.chat_room_id == room_id).offset(skip).limit(limit).all()
    return messages
