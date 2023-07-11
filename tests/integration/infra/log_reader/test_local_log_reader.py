from pathlib import Path

import pytest

from src.infra.log_reader.local_log_reader import LocalLogReader


pytestmark = pytest.mark.asyncio

_current_path = Path(__file__).parent.resolve()


async def test__local_log_reader_should_succeed():
    log_reader = LocalLogReader(f"{_current_path}/games.log.sample")
    lines = [line async for line in log_reader.iterline()]
    assert (lines[0], lines[-1]) == ("20:34 ClientConnect: 2", "20:37 ShutdownGame:")


async def test__local_log_reader_should_raise_file_not_found_error():
    log_reader = LocalLogReader(f"{_current_path}/non-existent.log")
    with pytest.raises(FileNotFoundError):
        await log_reader.iterline().__anext__()
