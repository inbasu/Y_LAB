from typing import Annotated

from fastapi import HTTPException, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from database import crud, schemas

from .main import v1

Submenu = crud.SubmenuRepository()


# READ
@v1.get("/menus/{menu_id}/submenus")
async def get_submenus(menu_id: Annotated[int, Path(title="Submenu ID", ge=1)]):
    return await Submenu.get_submenus(to_menu=menu_id)


@v1.get("/menus/{menu_id}/submenus/{submenu_id}", response_class=JSONResponse)
async def get_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
):
    submenu = await Submenu.get_submenu(to_menu=menu_id, id=submenu_id)
    if submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return submenu


# Create
@v1.post("/menus/{menu_id}/submenus", response_class=JSONResponse, status_code=201)
async def create_new_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu: schemas.CreateSubMenu,
):
    submenu.to_menu = menu_id
    submenu = await Submenu.create_submenu(submenu)
    return submenu


# Update
@v1.patch(
    "/menus/{menu_id}/submenus/{submenu_id}",
    response_class=JSONResponse,
    status_code=200,
)
async def update_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu: schemas.UpdateSubMenu,
):
    submenu = await Submenu.update_submenu(submenu, to_menu=menu_id, id=submenu_id)
    if submenu is None:
        raise HTTPException(status_code=404)
    return submenu


# Delete
@v1.delete("/menus/{menu_id}/submenus/{submenu_id}")
async def delete_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
):
    result = await Submenu.delete_submenu(to_menu=menu_id, id=submenu_id)
    if not result:
        raise HTTPException(status_code=404)
    return {"ok": result}
