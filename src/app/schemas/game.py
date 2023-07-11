from pydantic import BaseModel, RootModel


class GameSchema(BaseModel):
    total_kills: int
    players: list[str]
    kills: dict[str, int]


class GamesOut(RootModel):
    root: dict[str, GameSchema]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "game_1": {
                        "total_kills": 45,
                        "players": ["Dono da bola", "Isgalamido", "Zeh"],
                        "kills": {
                            "Dono da bola": 5,
                            "Isgalamido": 18,
                            "Zeh": 20
                        }
                    },
                    "game_2": {
                        "total_kills": 80,
                        "players": ["Dono da bola", "Isgalamido", "Mocinha"],
                        "kills": {
                            "Dono da bola": 13,
                            "Isgalamido": 21,
                            "Mocinha": 40
                        }
                    }
                }
            ]
        }
    }
