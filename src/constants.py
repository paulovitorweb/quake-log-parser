import tomllib
from pathlib import Path

CWD = Path().resolve()

GAMES_LOG_FILE_NAME = "games.log"
GAMES_LOG_PATH = CWD.joinpath(GAMES_LOG_FILE_NAME)

PYPROJECT_PATH = CWD.joinpath("pyproject.toml")

with open(PYPROJECT_PATH, "r") as f:
    _pyproject_data = tomllib.loads(f.read())

PROJECT_NAME = _pyproject_data["tool"]["poetry"]["name"]
PROJECT_VERSION = _pyproject_data["tool"]["poetry"]["version"]
PROJECT_DESCRIPTION = _pyproject_data["tool"]["poetry"]["description"]
