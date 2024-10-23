from pydantic import BaseModel
from typing import Optional, List

class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str]
    user_id: str

class ChatResponse(BaseModel):
    response: str
    sources: List[dict]
    conversation_id: str
