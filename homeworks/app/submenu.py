from typing import Annotated

from fastapi import Depends, HTTPException, Path
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database import crud, schemas
from database.database import get_db

from .main import v1


# READ
@v1.get("/menus/{menu_id}/submenus")
def get_all_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    db: Session = Depends(get_db),
):
    return crud.get_all_submenus(db, menu_id)


@v1.get("/menus/{menu_id}/submenus/{submenu_id}", response_class=JSONResponse)
def get_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    db: Session = Depends(get_db),
):
    submenu = crud.get_submenu_by_id(db, menu_id=menu_id, submenu_id=submenu_id)
    if submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    d_submenu = submenu.__dict__
    d_submenu["id"] = str(d_submenu["id"])
    d_submenu["dishes_count"] = submenu.dishes_in
    return d_submenu


# Create
@v1.post("/menus/{menu_id}/submenus", response_class=JSONResponse, status_code=201)
def create_new_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu: schemas.CreateSubMenu,
    db: Session = Depends(get_db),
):
    submenu.to_menu = menu_id
    submenu = crud.create_submenu(db, submenu)
    submenu.id = str(submenu.id)
    return submenu


# Update
@v1.patch(
    "/menus/{menu_id}/submenus/{submenu_id}",
    response_class=JSONResponse,
    status_code=200,
)
def update_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu: schemas.UpdateSubMenu,
    db: Session = Depends(get_db),
):
    submenu = crud.update_submenu_by_id(
        db, submenu, menu_id=menu_id, submenu_id=submenu_id
    )
    if submenu is None:
        raise HTTPException(status_code=404)
    return submenu


# Delete
@v1.delete("/menus/{menu_id}/submenus/{submenu_id}")
def delete_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    db: Session = Depends(get_db),
):
    result = crud.delte_submenu_by_id(db, menu_id, submenu_id)
    if not result:
        raise HTTPException(status_code=404)
    return {"ok": result}
