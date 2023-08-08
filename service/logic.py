import re
from abc import ABC

from fastapi.encoders import jsonable_encoder

from cache.crud import Cache
from database import crud
from database.database import Base
from database.schemas import BaseModel


class BaseService(ABC):
    database: crud.ModelRepository
    cache: Cache = Cache()

    async def create(self, create_menu) -> Base | None:
        item: Base = await self.database.create(create_menu)
        return item

    async def get_all(self, url, **kwargs) -> list[Base]:
        all_items: list[Base] | None = await self.cache.get(url)
        if not all_items:
            all_items = await self.database.get_all(**kwargs)
            await self.cache.set(url, jsonable_encoder(all_items))
        return all_items

    async def get(self, url, **kwargs) -> Base | None:
        item = await self.cache.get(url)
        if not item:
            item = await self.database.get(**kwargs)
            await self.cache.set(url, jsonable_encoder(item))
        return item

    async def update_all_cache(self, url, **kwargs) -> None:
        if 'id' in kwargs.keys():
            kwargs.pop('id')
        all_items = await self.database.get_all(**kwargs)
        await self.cache.set(cut_url(url), jsonable_encoder(all_items))

    async def update(self, update_model: BaseModel, url, **kwargs) -> Base | None:
        item = await self.database.update(update_model, **kwargs)
        await self.cache.set(url, jsonable_encoder(item))
        await self.update_all_cache(url, **kwargs)
        return item

    async def delete(self, url, **kwargs) -> bool:
        await self.cache.delete(url)
        result = await self.database.delete(**kwargs)
        await self.update_all_cache(url, **kwargs)
        return result


class MenuService(BaseService):

    def __init__(self) -> None:
        self.database = crud.MenuRepository()


class SubMenuService(BaseService):
    def __init__(self) -> None:
        self.database = crud.SubMenuRepository()


class DishService(BaseService):
    def __init__(self) -> None:
        self.database = crud.DishRepository()


def cut_url(url: str) -> str:
    return re.sub(r'(/\d+)$', '', url)
