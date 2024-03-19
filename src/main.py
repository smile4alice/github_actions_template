from fastapi import FastAPI

from src.sandbox.routes import sandbox_router

app = FastAPI(
    title="sand_app",
)

app.include_router(sandbox_router, prefix="/api/v1")
