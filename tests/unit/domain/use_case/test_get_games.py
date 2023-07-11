from unittest.mock import Mock

import pytest

from src.domain.service.parse_log import ParseLogService
from src.domain.use_case.get_games import GetGamesUseCase


pytestmark = pytest.mark.asyncio


async def test__get_games_use_case_should_succeed():
    service_mock = Mock(spec=ParseLogService)
    service_mock.parse.return_value = {"foo": "bar"}
    use_case = GetGamesUseCase(service_mock)
    assert await use_case.exec() == {"foo": "bar"}


async def test__get_games_use_case_should_raise_error():
    service_mock = Mock(spec=ParseLogService)
    service_mock.parse.side_effect = Exception("Houston, we have a problem")
    use_case = GetGamesUseCase(service_mock)
    with pytest.raises(Exception, match="Houston, we have a problem"):
        await use_case.exec()
