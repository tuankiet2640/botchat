from fastapi import FastAPI
from py_eureka_client import eureka_client

app = FastAPI()

# Initialize Eureka client
async def init_eureka_client():
    await eureka_client.init_async(
        eureka_server="http://localhost:8761/eureka",
        app_name="chatbot-service",
        instance_port=8000,
    )

@app.on_event("startup")
async def startup_event():
    await init_eureka_client()
