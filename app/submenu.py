from typing import Annotated

from database import crud, schemas
from database.database import get_db
from fastapi import Depends, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from .main import v1


# READ
@v1.get("/menus/{menu_id}/submenus")
def get_all_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    db: Session = Depends(get_db),
):
    return jsonable_encoder(crud.get_all_submenus(db, menu_id))


@v1.get("/menus/{menu_id}/submenus/{submenu_id}", response_class=JSONResponse)
def get_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    db: Session = Depends(get_db),
):
    submenu = crud.get_submenu_by_id(db, menu_id=menu_id, submenu_id=submenu_id)
    if submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    respnose = submenu.__dict__
    respnose["dishes_count"] = submenu.dishes_in
    return jsonable_encoder(respnose)


# Create
@v1.post("/menus/{menu_id}/submenus", response_class=JSONResponse, status_code=201)
def create_new_submenu(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu: schemas.CreateSubMenu,
    db: Session = Depends(get_db),
):
    submenu.to_menu = menu_id
    submenu = crud.create_submenu(db, submenu)
    return jsonable_encoder(submenu)


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
    return jsonable_encoder(submenu)


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
