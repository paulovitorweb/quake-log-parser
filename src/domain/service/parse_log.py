from dataclasses import dataclass

from src.domain.dto.game import Game
from src.domain.interface.log_reader import LogReader


@dataclass
class ParseLogService:
    log_reader: LogReader

    async def parse(self) -> dict[str, Game]:
        pass
