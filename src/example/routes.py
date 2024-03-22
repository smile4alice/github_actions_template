from fastapi import APIRouter
from fastapi.responses import JSONResponse

example_router = APIRouter(prefix="/example")


@example_router.get("")
async def get_example():
    return JSONResponse({"test": "OK"})
