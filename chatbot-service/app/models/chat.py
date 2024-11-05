from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ChatRequest(BaseModel):
    message: str
    conversation_id: str
    user_id: str
    timestamp: datetime = datetime.now()


class ChatResponse(BaseModel):
    response: str
    sources: List[str]
    timestamp: datetime = datetime.now()


class ChatHistory(BaseModel):
    conversation_id: str
    user_id: str
    messages: List[ChatRequest]
    responses: List[ChatResponse]
    timestamp: datetime = datetime.now()
