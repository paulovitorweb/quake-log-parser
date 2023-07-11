from typing import Protocol, AsyncGenerator


class LogReader(Protocol):
    async def iterline(self) -> AsyncGenerator[str, None]: ...
