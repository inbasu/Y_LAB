from sqlalchemy import func
from sqlalchemy.orm import Session

from . import database, schemas


# Menu crud
class MenuRepository:
    def __init__(self) -> None:
        self.__db: Session = database.get_db()
        self.model = schemas.Menu

    async def get_menus(self) -> list[schemas.Menu]:
        return self.__db.query(database.Menu).all()

    async def get_menu(self, **kwargs) -> schemas.Menu | None:
        return self.__db.query(database.Menu).filter_by(**kwargs).first()

    async def create_menu(self, menu: schemas.CreateMenu) -> schemas.Menu:
        menu = database.Menu(title=menu.title, description=menu.description)
        self.__db.add(menu)
        self.__db.commit()
        self.__db.refresh(menu)
        return menu

    async def update_menu(
        self, updated_menu: schemas.UpdateMenu, **kwargs
    ) -> schemas.Menu | None:
        menu = self.__db.query(database.Menu).filter_by(**kwargs).first()
        if menu is None:
            return menu
        menu.title = updated_menu.title
        menu.description = updated_menu.description
        self.__db.add(menu)
        self.__db.commit()
        self.__db.refresh(menu)
        return menu

    async def delte_menu(self, **kwargs) -> None:
        self.__db.query(database.Menu).filter_by(**kwargs).delete()
        self.__db.commit()


# Sub menu crud
class SubmenuRepository:
    def __init__(self) -> None:
        self.__db: Session = database.get_db()
        self.model = schemas.SubMenu

    async def get_submenus(self, **kwargs) -> list[schemas.SubMenu]:
        return self.__db.query(database.SubMenu).filter_by(**kwargs).all()

    async def get_submenu(self, **kwargs) -> schemas.SubMenu | None:
        return self.__db.query(database.SubMenu).filter_by(**kwargs).first()

    async def create_submenu(self, submenu: schemas.CreateSubMenu) -> schemas.SubMenu:
        submenu = database.SubMenu(
            title=submenu.title,
            description=submenu.description,
            to_menu=submenu.to_menu,
        )
        self.__db.add(submenu)
        self.__db.commit()
        self.__db.refresh(submenu)
        return submenu

    async def update_submenu(
        self, p_submenu: schemas.UpdateSubMenu, **kwargs
    ) -> schemas.SubMenu | None:
        submenu = self.__db.query(database.SubMenu).filter_by(**kwargs).first()
        if submenu is None:
            return submenu
        submenu.title = p_submenu.title
        submenu.description = p_submenu.description
        self.__db.add(submenu)
        self.__db.commit()
        self.__db.refresh(submenu)
        return submenu

    async def delete_submenu(self, **kwargs) -> bool:
        query = self.__db.query(database.SubMenu).filter_by(**kwargs)
        if not query:
            return False
        query.delete()
        self.__db.commit()
        return True


# Dishes CRUD
class DishRepository:
    def __init__(self) -> None:
        self.__db: Session = database.get_db()
        self.model = schemas.Dish

    async def get_dishes(self, **kwargs) -> list[schemas.Dish]:
        return self.__db.query(database.Dish).filter_by(**kwargs).all()

    async def get_dish(self, **kwargs) -> schemas.Dish | None:
        return self.__db.query(database.Dish).filter_by(**kwargs).first()

    async def create_dish(self, dish: schemas.CreateDish) -> schemas.Dish:
        dish = database.Dish(
            title=dish.title,
            description=dish.description,
            price=dish.price,
            to_submenu=dish.to_submenu,
        )
        self.__db.add(dish)
        self.__db.commit()
        self.__db.refresh(dish)
        return dish

    async def update_dish(
        self, p_dish: schemas.UpdateDish, **kwargs
    ) -> schemas.Dish | None:
        dish = self.__db.query(database.Dish).filter_by(**kwargs).first()
        if dish is None:
            return dish
        dish.title = p_dish.title
        dish.description = p_dish.description
        dish.price = p_dish.price
        self.__db.add(dish)
        self.__db.commit()
        self.__db.refresh(dish)
        return dish

    async def delte_dish(self, **kwargs) -> bool:
        query = self.__db.query(database.Dish).filter_by(**kwargs)
        if not query:
            return False
        query.delete()
        self.__db.commit()
        return True
