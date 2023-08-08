import json
from typing import Any

from redis import Redis

from .database import r


class Cache:
    def __init__(self) -> None:
        self.db: Redis = r

    async def get(self, url: str) -> Any:
        data = self.db.get(url)
        if data:
            return json.loads(data)
        return []

    async def set(self, url: str, data: Any) -> None:
        data = json.dumps(data)
        self.db.set(url, data)

    async def delete(self, url: str) -> None:
        _, data = self.db.scan(match=f'{url}*')
        self.db.delete(*data)
