import pytest

from httpx import AsyncClient

from src.app.schemas.game import GamesOut
from tests.e2e.utils import validate_response_body


pytestmark = pytest.mark.asyncio


async def test__get_games_should_succeed(test_app: AsyncClient):
    response = await test_app.get("/games/")
    assert response.status_code == 200
    is_valid, exc = validate_response_body(response.json(), GamesOut)
    assert is_valid, exc


async def test__healthcheck(test_app: AsyncClient):
    response = await test_app.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}
