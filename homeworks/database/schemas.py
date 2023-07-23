from pydantic import BaseModel


# Memu
class MenuBase(BaseModel):
    title: str
    description: str | None = None


class CreateMenu(MenuBase):
    pass


class UpdateMenu(MenuBase):
    title: str
    description: str


class Menu(MenuBase):
    id: int

    class Config:
        from_attributes = True


# submenu
class SubMenuBase(BaseModel):
    title: str
    description: str | None = None
    to_menu: int | None = None


class CreateSubMenu(SubMenuBase):
    pass


class UpdateSubMenu(SubMenuBase):
    title: str
    description: str


class SubMenu(SubMenuBase):
    id: int

    class Config:
        from_attributes = True


# dishes
class DishBase(BaseModel):
    title: str
    description: str | None = None
    price: float
    to_submenu: int | None = None


class CreateDish(DishBase):
    pass


class UpdateDish(DishBase):
    title: str
    description: str


class Dish(DishBase):
    id: int

    class Config:
        from_attributes = True
