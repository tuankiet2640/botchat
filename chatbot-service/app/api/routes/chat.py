from fastapi import APIRouter, Body
from typing import List
from datetime import datetime
from pydantic import BaseModel
from app.config.settings import settings
from app.services.azure_openai import AzureOpenAIService
from app.services.azure_ai_search import AzureSearchService
from app.services.chat_orchestrator import ChatOrchestrator
from app.models.chat import ChatRequest, ChatResponse

chat_router = APIRouter()

# Initialize the ChatOrchestrator
azure_openai_service = AzureOpenAIService(
    api_key=settings.AZURE_OPENAI_API_KEY,
    engine=settings.AZURE_OPENAI_ENGINE
)
azure_search_service = AzureSearchService(
    endpoint=settings.AZURE_SEARCH_ENDPOINT,
    index_name=settings.AZURE_SEARCH_INDEX,
    api_key=settings.AZURE_SEARCH_API_KEY
)
chat_orchestrator = ChatOrchestrator(
    openai_service=azure_openai_service,
    search_service=azure_search_service
)


@chat_router.post("/chat", response_model=ChatResponse)
async def chat(chat_request: ChatRequest = Body(...)):
    """
    Process a chat request and generate a response.

    Args:
        chat_request (ChatRequest): The incoming chat request.

    Returns:
        ChatResponse: The chatbot's response.
    """
    response = await chat_orchestrator.process_message(
        message=chat_request.message,
        conversation_id=chat_request.conversation_id,
        user_id=chat_request.user_id
    )
    return ChatResponse(**response)