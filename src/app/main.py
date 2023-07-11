from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import ORJSONResponse

from src.app.schemas.game import GamesOut
from src.domain.service.parse_log import ParseLogService
from src.domain.use_case.get_games import GetGamesUseCase
from src.infra.log_reader.local_log_reader import LocalLogReader

app = FastAPI()


_root_path = Path().resolve()


@app.get("/games/", response_model=GamesOut, status_code=200, response_class=ORJSONResponse)
async def get_games(file: str = "games.log"):
    log_reader = LocalLogReader(f"{_root_path}/{file}")
    parse_log_service = ParseLogService(log_reader)
    use_case = GetGamesUseCase(parse_log_service)

    try:
        result = await use_case.exec()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="file not found")

    return ORJSONResponse(result)
