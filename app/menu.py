from typing import Annotated

from fastapi import HTTPException, Path
from fastapi.responses import JSONResponse

from database import crud, schemas

from .main import v1

Menu = crud.MenuRepository()


# CREATE
@v1.post("/menus", response_class=JSONResponse, status_code=201)
async def create_new_menu(menu: schemas.CreateMenu):
    return await Menu.create_menu(menu)


# READ
@v1.get("/menus")
async def get_menus():
    return await Menu.get_menus()


@v1.get("/menus/{menu_id}")
async def get_menu(menu_id: Annotated[int, Path(title="Menu ID", ge=1)]):
    menu = await Menu.get_menu(id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return menu


# UPDATE
@v1.patch("/menus/{menu_id}", response_class=JSONResponse, status_code=200)
async def update_menu(
    menu_id: Annotated[int, Path(title="Menu ID", ge=1)],
    menu: schemas.UpdateMenu,
):
    menu = await Menu.update_menu(menu, id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404)
    return menu


# DELTE
@v1.delete("/menus/{menu_id}")
async def delete_menu(menu_id: Annotated[int, Path(title="Menu ID", ge=1)]):
    await Menu.delte_menu(id=menu_id)
    return {"ok": True}
