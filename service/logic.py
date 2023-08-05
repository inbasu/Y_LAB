from abc import ABC

from database import crud
from database.schemas import BaseModel, CreateMenu, Menu, UpdateMenu


class BaseService(ABC):
    database: crud.ModelRepository

    async def create(self, create_menu: CreateMenu) -> BaseModel:
        item = await self.database.create(create_menu)
        return item

    async def get_all(self, **kwargs) -> list[BaseModel]:
        all_items = await self.database.get_all(**kwargs)
        return all_items

    async def get(self, **kwargs) -> Menu | None:
        item: BaseModel | None = await self.database.get(**kwargs)
        return item

    async def update(self, update_model: UpdateMenu, **kwargs) -> BaseModel | None:
        item: BaseModel | None = await self.database.update(update_model, **kwargs)
        return item

    async def delete(self, **kwargs) -> bool:
        return await self.database.delete()


class MenuService(BaseService):
    def __init__(self) -> None:
        self.database = crud.MenuRepository()


class SubMenuService(BaseService):
    def __init__(self) -> None:
        self.database = crud.SubMenuRepository()


class DishService(BaseService):
    def __init__(self) -> None:
        self.database = crud.DishRepository()
