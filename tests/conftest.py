import asyncio
from typing import Generator

import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from src.app.main import app


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture()
async def test_app():
    async with LifespanManager(app):
        async with AsyncClient(
            app=app, base_url="http://127.0.0.1:8000", follow_redirects=True
        ) as ac:
            yield ac
