from fastapi import FastAPI
from routers.router import router as router

app = FastAPI()

app.include_router(router, tags=["Social_network"], prefix="/api")
