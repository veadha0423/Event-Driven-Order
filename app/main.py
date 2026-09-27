from fastapi import FastAPI
from app.api.v1.router import router as v1_router

def create_app() -> FastAPI:
    app = FastAPI(title="Event Driver orders",version="1.0.0")
    #Mount V1 API routes 
    app.include_router(v1_router,prefix="/api/v1")

    return app

app = create_app()