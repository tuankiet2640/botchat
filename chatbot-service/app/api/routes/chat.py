# from fastapi import APIRouter, Depends, HTTPException
# from app.services.chat_orchestrator import ChatOrchestrator
# from app.models.chat import ChatRequest, ChatResponse
#
# router = APIRouter()
#
# @router.post("/chat", response_model=ChatResponse)
# async def chat(
#     request: ChatRequest,
#     chat_orchestrator: ChatOrchestrator = Depends()
# ):
#     try:
#         response = await chat_orchestrator.process_message(
#             message=request.message,
#             conversation_id=request.conversation_id,
#             user_id=request.user_id
#         )
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))