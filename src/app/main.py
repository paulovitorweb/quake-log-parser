from fastapi import FastAPI, HTTPException
from fastapi.responses import ORJSONResponse

from src.constants import GAMES_LOG_PATH
from src.app.schemas.game import GamesOut
from src.app.schemas.healthcheck import HealthCheckOut
from src.domain.service.parse_log import ParseLogService
from src.domain.use_case.get_games import GetGamesUseCase
from src.infra.log_reader.local_log_reader import LocalLogReader

app = FastAPI()


@app.get("/games/", response_model=GamesOut, status_code=200, response_class=ORJSONResponse)
async def get_games():
    log_reader = LocalLogReader(str(GAMES_LOG_PATH))
    parse_log_service = ParseLogService(log_reader)
    use_case = GetGamesUseCase(parse_log_service)

    try:
        result = await use_case.exec()
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="internal server error")

    return ORJSONResponse(result)


@app.get("/healthcheck/", response_model=HealthCheckOut, status_code=200)
async def healthcheck():
    return {"status": "alive"}
