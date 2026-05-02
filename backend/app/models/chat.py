"""Chat Model"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class ChatRoom(Base):
    __tablename__ = "chat_rooms"
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    technician_id = Column(Integer, ForeignKey("technicians.id"), nullable=False)
    booking_id = Column(Integer, nullable=True)  # Optional: related to a booking
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    client = relationship("User", back_populates="chat_rooms")
    technician = relationship("Technician", back_populates="chat_rooms")
    messages = relationship("ChatMessage", back_populates="chat_room", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<ChatRoom {self.id}>"

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    chat_room_id = Column(Integer, ForeignKey("chat_rooms.id"), nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    is_read = Column(Integer, default=0, nullable=False)  # 0: unread, 1: read
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    chat_room = relationship("ChatRoom", back_populates="messages")
    
    def __repr__(self):
        return f"<ChatMessage {self.id}>"
