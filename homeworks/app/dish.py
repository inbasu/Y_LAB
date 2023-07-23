from typing import Annotated

from fastapi import Depends, HTTPException, Path
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database import crud, schemas
from database.database import get_db

from .main import v1


# READ
@v1.get("/menus/{menu_id}/submenus/{submenu_id}/dishes")
def get_all_dishes(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    db: Session = Depends(get_db),
):
    return crud.get_all_dishes(db, submenu_id)


@v1.get(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
    response_class=JSONResponse,
)
def get_dish(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    dish_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    db: Session = Depends(get_db),
):
    dish = crud.get_dish_by_id(db, submenu_id=submenu_id, dish_id=dish_id)
    if dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    dish.id = str(dish.id)
    return dish


# Create
@v1.post(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes",
    response_class=JSONResponse,
    status_code=201,
)
def create_new_dish(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    dish: schemas.CreateDish,
    db: Session = Depends(get_db),
):
    dish.to_submenu = submenu_id
    dish = crud.create_dish(db, dish)
    dish.id = str(dish.id)
    return dish


# Update
@v1.patch(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
    response_class=JSONResponse,
    status_code=200,
)
def update_dish(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    dish_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    dish: schemas.UpdateDish,
    db: Session = Depends(get_db),
):
    dish = crud.update_dish_by_id(db, dish, submenu_id=submenu_id, dish_id=dish_id)
    if dish is None:
        raise HTTPException(status_code=404)
    return dish


# Delete
@v1.delete("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
def delete_dish(
    menu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    dish_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    db: Session = Depends(get_db),
):
    result = crud.delte_dish_by_id(db, submenu_id=submenu_id, dish_id=dish_id)
    if not result:
        raise HTTPException(status_code=404)
    return {"ok": result}
