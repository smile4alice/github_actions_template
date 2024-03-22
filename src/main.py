from fastapi import FastAPI

from src.example.routes import example_router

app = FastAPI(
    title="sand_app",
)

app.include_router(example_router, prefix="/api/v1")
