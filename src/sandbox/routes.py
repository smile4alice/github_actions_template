from fastapi import APIRouter
from fastapi.responses import JSONResponse

sandbox_router = APIRouter(prefix="/sandbox")


@sandbox_router.get("")
async def get_sand():
    return JSONResponse({"test": "OK"})
