from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import JSONResponse

from database import schemas
from service.logic import DishService, MenuService, SubMenuService

app: FastAPI = FastAPI()
v1: FastAPI = FastAPI()

app.mount('/api/v1', v1)

Menu = MenuService()
Submenu = SubMenuService()
Dish = DishService()


# CREATE
@v1.post('/menus', response_class=JSONResponse, status_code=201)
async def create_new_menu(menu: schemas.CreateMenu):
    return await Menu.create(menu)


# READ
@v1.get('/menus')
async def get_menus(request: Request):
    url = str(request.url)
    return await Menu.get_all(url=url)


@v1.get('/menus/{menu_id}')
async def get_menu(
    menu_id: Annotated[int, Path(title='Menu ID', ge=1)], request: Request
):
    url = str(request.url)
    menu = await Menu.get(url=url, id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail='menu not found')
    return menu


# UPDATE
@v1.patch('/menus/{menu_id}', response_class=JSONResponse, status_code=200)
async def update_menu(
    menu_id: Annotated[int, Path(title='Menu ID', ge=1)],
    update_menu: schemas.UpdateMenu,
    request: Request,
):
    url = str(request.url)
    menu = await Menu.update(update_menu, url=url, id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404)
    return menu


# DELTE
@v1.delete('/menus/{menu_id}')
async def delete_menu(
    menu_id: Annotated[int, Path(title='Menu ID', ge=1)], request: Request
):
    url = str(request.url)
    await Menu.delete(url, id=menu_id)
    return {'ok': True}


# READ
@v1.get('/menus/{menu_id}/submenus')
async def get_submenus(menu_id: Annotated[int, Path(title='Submenu ID', ge=1)], request: Request):
    url = str(request.url)
    return await Submenu.get_all(url=url, to_menu=menu_id)


@v1.get('/menus/{menu_id}/submenus/{submenu_id}', response_class=JSONResponse)
async def get_submenu(
    menu_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    submenu_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    request: Request
):
    url = str(request.url)
    submenu = await Submenu.get(url=url, to_menu=menu_id, id=submenu_id)
    if submenu is None:
        raise HTTPException(status_code=404, detail='submenu not found')
    return submenu


# Create
@v1.post('/menus/{menu_id}/submenus', response_class=JSONResponse, status_code=201)
async def create_new_submenu(
    menu_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    submenu: schemas.CreateSubMenu
):
    submenu.to_menu = menu_id
    submenu = await Submenu.create(submenu)
    return submenu


# Update
@v1.patch(
    '/menus/{menu_id}/submenus/{submenu_id}',
    response_class=JSONResponse,
    status_code=200,
)
async def update_submenu(
    menu_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    submenu_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    update_submenu: schemas.UpdateSubMenu,
    request: Request
):
    url = str(request.url)
    submenu = await Submenu.update(update_submenu, url=url, to_menu=menu_id, id=submenu_id)
    if submenu is None:
        raise HTTPException(status_code=404)
    return submenu


# Delete
@v1.delete('/menus/{menu_id}/submenus/{submenu_id}')
async def delete_submenu(
    menu_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    submenu_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    request: Request
):
    url = str(request.url)
    result = await Submenu.delete(url=url, to_menu=menu_id, id=submenu_id)
    if not result:
        raise HTTPException(status_code=404)
    return {'ok': result}


# READ
@v1.get('/menus/{menu_id}/submenus/{submenu_id}/dishes')
async def get_dishes(submenu_id: Annotated[int, Path(title='Submenu ID', ge=1)], request: Request):
    url = str(request.url)
    return await Dish.get_all(url=url, to_submenu=submenu_id)


@v1.get(
    '/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}',
    response_class=JSONResponse,
)
async def get_dish(
    submenu_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    dish_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    request: Request
):
    url = str(request.url)
    dish = await Dish.get(url=url, to_submenu=submenu_id, id=dish_id)
    if dish is None:
        raise HTTPException(status_code=404, detail='dish not found')
    return dish


# Create
@v1.post(
    '/menus/{menu_id}/submenus/{submenu_id}/dishes',
    response_class=JSONResponse,
    status_code=201,
)
async def create_new_dish(
    submenu_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    dish: schemas.CreateDish,
):
    dish.to_submenu = submenu_id
    dish = await Dish.create(dish)
    return dish


# Update
@v1.patch(
    '/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}',
    status_code=200,
)
async def update_dish(
    submenu_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    dish_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    update_dish: schemas.UpdateDish,
    request: Request
):
    url = str(request.url)
    dish = await Dish.update(update_dish, url=url, to_submenu=submenu_id, id=dish_id)
    if dish is None:
        raise HTTPException(status_code=404)
    return dish


# Delete
@v1.delete('/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}')
async def delete_dish(
    submenu_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    dish_id: Annotated[int, Path(title='Submenu ID', ge=1)],
    request: Request
):
    url = str(request.url)
    result = await Dish.delete(url=url, to_submenu=submenu_id, id=dish_id)
    if not result:
        raise HTTPException(status_code=404)
    return {'ok': result}
