from typing import AsyncGenerator
from dataclasses import dataclass

import aiofiles


@dataclass
class LocalLogReader:
    file_path: str

    async def iterline(self) -> AsyncGenerator[str, None]:
        async with aiofiles.open(self.file_path) as file:
            async for line in file:
                yield line.strip()
