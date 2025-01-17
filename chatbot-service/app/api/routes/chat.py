from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

# Import the ChatOrchestrator from your existing module
from app.services.chat_orchestrator import ChatOrchestrator

# Create a router
chat_router = APIRouter()


# Create a Pydantic model for the request
class ChatRequest(BaseModel):
    query: str
    chat_history: List[dict] = []  # Optional chat history


# Create a Pydantic model for the response
class ChatResponse(BaseModel):
    response: str
    sources: List[str] = []


# Initialize the ChatOrchestrator (consider using dependency injection in a real-world app)
chat_orchestrator = ChatOrchestrator()


@chat_router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Chat endpoint that processes user queries using Azure AI services

    :param request: ChatRequest containing user query and optional chat history
    :return: ChatResponse with AI-generated response
    """
    try:
        # Process the query
        response = chat_orchestrator.process_query(request.query)

        # You might want to enhance this to also return sources
        return ChatResponse(
            response=response,
            sources=[]  # You can modify the orchestrator to return sources if needed
        )

    except Exception as e:
        # Proper error handling
        raise HTTPException(status_code=500, detail=str(e))