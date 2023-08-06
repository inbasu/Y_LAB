import json

from .database import r


class Cache:
    def __init__(self) -> None:
        self.db = r

    async def get(self, url):
        data = self.db.get(url)
        if data:
            return json.loads(data)
        return []

    async def set(self, url, data) -> None:
        data = json.dumps(data)
        self.db.set(url, data)

    async def delete(self, url) -> None:
        self.db.delete(url)
