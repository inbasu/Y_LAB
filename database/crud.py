from sqlalchemy.orm import Session
from sqlalchemy import func

from . import database, schemas


# Menu crud
def get_all_menus(db: Session):
    return db.query(database.Menu).all()


def get_menu_by_id(db: Session, menu_id: int):
    return db.query(database.Menu).filter(database.Menu.id == menu_id).first()


def create_menu(db: Session, menu: schemas.CreateMenu):
    menu = database.Menu(title=menu.title, description=menu.description)
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu


def update_menu_bu_id(db: Session, p_menu: schemas.UpdateMenu, menu_id):
    menu = db.query(database.Menu).filter(database.Menu.id == menu_id).first()
    if menu is None:
        return menu
    menu.title = p_menu.title
    menu.description = p_menu.description
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu


def delte_menu_by_id(db: Session, menu_id: int):
    db.query(database.Menu).filter(database.Menu.id == menu_id).delete()
    db.commit()


# Sub menu crud
def get_all_submenus(db: Session, menu_id: int):
    return db.query(database.SubMenu).filter(database.SubMenu.to_menu == menu_id).all()


def get_submenu_by_id(db: Session, menu_id: int, submenu_id: int):
    return (
        db.query(database.SubMenu)
        .filter(database.SubMenu.to_menu == menu_id, database.SubMenu.id == submenu_id)
        .first()
    )


def create_submenu(db: Session, submenu: schemas.CreateSubMenu):
    submenu = database.SubMenu(
        title=submenu.title, description=submenu.description, to_menu=submenu.to_menu
    )
    db.add(submenu)
    db.commit()
    db.refresh(submenu)
    return submenu


def update_submenu_by_id(
    db: Session, p_submenu: schemas.UpdateSubMenu, menu_id: int, submenu_id: int
):
    submenu = (
        db.query(database.SubMenu)
        .filter(database.SubMenu.to_menu == menu_id, database.SubMenu.id == submenu_id)
        .first()
    )
    if submenu is None:
        return submenu
    submenu.title = p_submenu.title
    submenu.description = p_submenu.description
    db.add(submenu)
    db.commit()
    db.refresh(submenu)
    return submenu


def delte_submenu_by_id(db: Session, menu_id: int, submenu_id: int):
    result = (
        db.query(database.SubMenu)
        .filter(database.SubMenu.to_menu == menu_id, database.SubMenu.id == submenu_id)
        .delete()
    )
    db.commit()
    return bool(result)


# Dishes CRUD
def get_all_dishes(db: Session, menu_id: int):
    return db.query(database.Dish).filter(database.Dish.to_submenu == menu_id).all()


def get_dish_by_id(db: Session, dish_id: int, submenu_id: int):
    return (
        db.query(database.Dish)
        .filter(database.Dish.to_submenu == submenu_id, database.Dish.id == dish_id)
        .first()
    )


def create_dish(db: Session, dish: schemas.CreateDish):
    dish = database.Dish(
        title=dish.title,
        description=dish.description,
        price=dish.price,
        to_submenu=dish.to_submenu,
    )
    db.add(dish)
    db.commit()
    db.refresh(dish)
    return dish


def update_dish_by_id(
    db: Session, p_dish: schemas.UpdateDish, submenu_id: int, dish_id: int
):
    dish = (
        db.query(database.Dish)
        .filter(database.Dish.to_submenu == submenu_id, database.Dish.id == dish_id)
        .first()
    )
    if dish is None:
        return dish
    dish.title = p_dish.title
    dish.description = p_dish.description
    dish.price = p_dish.price
    db.add(dish)
    db.commit()
    db.refresh(dish)
    return dish


def delte_dish_by_id(db: Session, submenu_id: int, dish_id: int):
    result = (
        db.query(database.Dish)
        .filter(database.Dish.to_submenu == submenu_id, database.Dish.id == dish_id)
        .delete()
    )
    db.commit()
    return bool(result)


# SUB ACTIONS
def menu_count(db: Session, submenu_id):
    pass


def submenu_count(db: Session, submenu_id):
    return (
        db.query(database.Dish).filter(database.Dish.to_submenu == submenu_id).count()
    )
