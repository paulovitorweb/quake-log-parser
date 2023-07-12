from pathlib import Path

CWD = Path().resolve()
GAMES_LOG_FILE_NAME = "games.log"
GAMES_LOG_PATH = CWD.joinpath(GAMES_LOG_FILE_NAME)
