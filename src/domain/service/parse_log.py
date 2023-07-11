import re
from typing import Optional
from dataclasses import dataclass
from collections import defaultdict

from src.domain.dto.game import Game
from src.domain.interface.log_reader import LogReader


INIT_GAME_REGEX = r"\d+:\d+ InitGame:"
KILL_REGEX = r"\d+:\d+ Kill: \d+ \d+ \d+: (.*?) killed (.*?) by"
WORLD_NICK: str = "<world>"


@dataclass
class ParseLogService:
    log_reader: LogReader

    async def parse(self) -> dict[str, Game]:
        current_game: Optional[str] = None
        players: set[str] = set()
        total_kills: int = 0
        kills_by_player: dict[str, int] = defaultdict(int)
        games: dict[str, Game] = {}

        def index_current_game() -> None:
            games[current_game] = {
                "kills": dict(**kills_by_player),
                "players": sorted(list(players)),
                "total_kills": total_kills,
            }

        async for line in self.log_reader.iterline():
            if re.match(INIT_GAME_REGEX, line):
                if current_game:
                    index_current_game()
                    kills_by_player.clear()
                    total_kills = 0
                current_game = "game_{}".format(len(games) + 1)

            elif match := re.match(KILL_REGEX, line):
                killer_nick, killed_nick = match.group(1), match.group(2)

                if killer_nick == WORLD_NICK:
                    kills_by_player[killed_nick] -= 1
                elif killer_nick != killed_nick:
                    kills_by_player[killer_nick] += 1

                total_kills += 1

                if killer_nick != WORLD_NICK:
                    players.add(killer_nick)

                players.add(killed_nick)

        if current_game:
            index_current_game()

        return games
