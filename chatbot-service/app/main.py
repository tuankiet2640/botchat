from fastapi import FastAPI

app = FastAPI()

app.include_router(chat_router)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}