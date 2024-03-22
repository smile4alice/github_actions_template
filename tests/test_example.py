from httpx import AsyncClient
import pytest

from tests.conftest import API_PREFIX


EXAMPLE_ROUTE = API_PREFIX + "/example"


@pytest.fixture(scope="session")
async def example_data():
    data = {"test": "OK"}
    return data


async def test_get_list_team(ac: AsyncClient):
    response = await ac.get(EXAMPLE_ROUTE)
    assert response.status_code == 200
