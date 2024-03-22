from httpx import AsyncClient as AClient, ASGITransport
import pytest

from src.main import app

API_PREFIX = "/api/v1"


@pytest.fixture(scope="session")
async def ac():
    async with AClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
