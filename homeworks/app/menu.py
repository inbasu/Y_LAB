from typing import Annotated

from fastapi import Depends, HTTPException, Path
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database import crud, schemas
from database.database import get_db

from .main import v1


# CREATE
@v1.post("/menus", response_class=JSONResponse, status_code=201)
def create_new_menu(
    menu: schemas.CreateMenu,
    db: Session = Depends(get_db),
):
    menu = crud.create_menu(db, menu)
    menu.id = str(menu.id)
    return menu


# READ
@v1.get("/menus", response_model=list[schemas.Menu])
async def get_menus(db: Session = Depends(get_db)):
    return crud.get_all_menus(db)


@v1.get("/menus/{menu_id}", response_class=JSONResponse)
async def get_menu(
    menu_id: Annotated[int, Path(title="Menu ID", ge=1)],
    db: Session = Depends(get_db),
):
    menu = crud.get_menu_by_id(db, menu_id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    d_menu = menu.__dict__
    d_menu["id"] = str(menu.id)
    d_menu["submenus_count"] = menu.submenus_in
    d_menu["dishes_count"] = menu.dishes_in
    return d_menu


# UPDATE
@v1.patch("/menus/{menu_id}", response_class=JSONResponse, status_code=200)
def update_menu(
    menu_id: Annotated[int, Path(title="Menu ID", ge=1)],
    menu: schemas.UpdateMenu,
    db: Session = Depends(get_db),
):
    menu = crud.update_menu_bu_id(db, menu, menu_id)
    if menu is None:
        raise HTTPException(status_code=404)
    return menu


# DELTE
@v1.delete("/menus/{menu_id}")
def delete_menu(
    menu_id: Annotated[int, Path(title="Menu ID", ge=1)],
    db: Session = Depends(get_db),
):
    crud.delte_menu_by_id(db, menu_id)
    return {"ok": True}
