from dataclasses import dataclass

from src.domain.dto.game import Game
from src.domain.service.parse_log import ParseLogService


@dataclass
class GetGamesUseCase:
    parse_log_service: ParseLogService

    async def exec(self) -> dict[str, Game]:
        return await self.parse_log_service.parse()
