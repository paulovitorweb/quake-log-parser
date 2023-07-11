from pathlib import Path
from typing import AsyncGenerator

import pytest
import pytest_asyncio
import aiofiles

from src.domain.dto.game import Game
from src.domain.service.parse_log import ParseLogService


pytestmark = pytest.mark.asyncio

_current_path = Path(__file__).parent.resolve()


class LogReaderMock:
    file_path: str = f"{_current_path}/games.log.sample"

    async def iterline(self) -> AsyncGenerator[str, None]:
        async with aiofiles.open(self.file_path) as file:
            async for line in file:
                yield line.strip()


class TestParseLogService:
    """
    Requirements:
    1. When `<world>` kills the player it loses -1 kill.
    2. `<world>` is not a player and should not appear in the player list or kill dictionary.
    3. `total_kills` are game kills, this includes `<world>` kills.
    """

    @pytest_asyncio.fixture(scope="module")
    async def sut(self):
        svc = ParseLogService(LogReaderMock())
        return await svc.parse()

    async def test__games_length(self, sut: dict[str, Game]):
        assert len(sut) == 7

    async def test__game_1(self, sut: dict[str, Game]):
        assert sut["game_1"] == {"kills": {}, "players": [], "total_kills": 0}

    async def test__game_2(self, sut: dict[str, Game]):
        assert sut["game_2"] == {"kills": {"Isgalamido": -7}, "players": ["Isgalamido", "Mocinha"], "total_kills": 11}

    async def test__game_3(self, sut: dict[str, Game]):
        assert sut["game_3"] == {
            "kills": {"Dono da Bola": -1, "Isgalamido": 1, "Zeh": -2},
            "players": ["Dono da Bola", "Isgalamido", "Mocinha", "Zeh"],
            "total_kills": 4,
        }

    async def test__game_4(self, sut: dict[str, Game]):
        assert sut["game_4"] == {
            "kills": {"Assasinu Credi": 12, "Dono da Bola": 9, "Isgalamido": 19, "Zeh": 20},
            "players": ["Assasinu Credi", "Dono da Bola", "Isgalamido", "Mocinha", "Zeh"],
            "total_kills": 105,
        }

    async def test__game_5(self, sut: dict[str, Game]):
        assert sut["game_5"] == {
            "kills": {"Assasinu Credi": -1, "Isgalamido": 2, "Zeh": 1},
            "players": ["Assasinu Credi", "Dono da Bola", "Isgalamido", "Mocinha", "Zeh"],
            "total_kills": 14,
        }

    async def test__game_6(self, sut: dict[str, Game]):
        assert sut["game_6"] == {
            "kills": {
                "Assasinu Credi": 1,
                "Dono da Bola": 2,
                "Isgalamido": 3,
                "Maluquinho": 0,
                "Oootsimo": 8,
                "Zeh": 7,
            },
            "players": [
                "Assasinu Credi",
                "Dono da Bola",
                "Isgalamido",
                "Mal",
                "Maluquinho",
                "Mocinha",
                "Oootsimo",
                "UnnamedPlayer",
                "Zeh",
            ],
            "total_kills": 29,
        }

    async def test__game_7(self, sut: dict[str, Game]):
        assert sut["game_7"] == {
            "kills": {"Assasinu Credi": 19, "Dono da Bola": 10, "Isgalamido": 14, "Mal": -3, "Oootsimo": 20, "Zeh": 8},
            "players": [
                "Assasinu Credi",
                "Chessus",
                "Dono da Bola",
                "Isgalamido",
                "Mal",
                "Maluquinho",
                "Mocinha",
                "Oootsimo",
                "UnnamedPlayer",
                "Zeh",
            ],
            "total_kills": 130,
        }
