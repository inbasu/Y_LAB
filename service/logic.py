from abc import ABC, abstractmethod

from database import crud
from database.schemas import CreateMenu, Dish, Menu, UpdateMenu


class BaseService(ABC):
    database: crud.ModelRepository

    async def create(self, create_menu: CreateMenu) -> Menu:
        menu = await self.database.create(create_menu)
        return menu

    async def get(self, **kwargs) -> Menu | None:
        item: Menu | None = await self.database.get(**kwargs)
        return item

    @abstractmethod
    async def update(self, update_model: UpdateMenu, **kwargs) -> Menu | None:
        pass

    async def delete(self, **kwargs) -> bool:
        return await self.database.delete()


class MenuService(BaseService):
    def __init__(self) -> None:
        self.database = crud.MenuRepository()

    async def update(self, update_model: UpdateMenu, **kwargs) -> Menu | None:
        item: Menu | None = await self.database.update(update_model, **kwargs)
        return item

    async def get_all(self) -> list[Menu]:
        all_items: list[Menu] = await self.database.get_all()
        return all_items


class SubMenuService(BaseService):
    def __init__(self) -> None:
        self.database = crud.SubMenuRepository()

    async def get_all(self, to_menu) -> list[Menu]:
        all_items: list[Menu] = await self.database.get_all(to_menu=to_menu)
        return all_items

    async def update(self, update_model: UpdateMenu, **kwargs) -> Menu | None:
        item: Menu | None = await self.database.update(update_model, **kwargs)
        return item


class DishService(BaseService):
    def __init__(self) -> None:
        self.database = crud.SubMenuRepository()

    async def get_all(self, to_submenu) -> list[Dish]:
        all_items: list[Menu] = await self.database.get_all(to_submenu=to_submenu)
        return all_items

    async def update(self, update_model: UpdateMenu, **kwargs) -> Menu | None:
        item: Menu | None = await self.database.update(update_model, **kwargs)
        return item
