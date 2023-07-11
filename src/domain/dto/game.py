from typing import TypedDict


class Game(TypedDict):
    total_kills: int
    players: list[str]
    kills: dict[str, int]
