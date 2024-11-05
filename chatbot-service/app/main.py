from fastapi import FastAPI
from app.api.routes.chat import chat_router

app = FastAPI()

app.include_router(chat_router, tags=["chat"], prefix="/api", responses={404: {"description": "Not found"}})
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}