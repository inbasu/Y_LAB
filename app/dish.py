from typing import Annotated

from fastapi import HTTPException, Path
from fastapi.responses import JSONResponse

from database import crud, schemas

from .main import v1

Dish = crud.DishRepository()


# READ
@v1.get("/menus/{menu_id}/submenus/{submenu_id}/dishes")
async def get_dishes(submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)]):
    return await Dish.get_dishes(to_submenu=submenu_id)


@v1.get(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
    response_class=JSONResponse,
)
async def get_dish(
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    dish_id: Annotated[int, Path(title="Submenu ID", ge=1)],
):
    dish = await Dish.get_dish(to_submenu=submenu_id, id=dish_id)
    if dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return dish


# Create
@v1.post(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes",
    response_class=JSONResponse,
    status_code=201,
)
async def create_new_dish(
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    dish: schemas.CreateDish,
):
    dish.to_submenu = submenu_id
    dish = await Dish.create_dish(dish)
    return dish


# Update
@v1.patch(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
    response_class=JSONResponse,
    status_code=200,
)
async def update_dish(
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    dish_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    dish: schemas.UpdateDish,
):
    dish = await Dish.update_dish(dish, to_submenu=submenu_id, id=dish_id)
    if dish is None:
        raise HTTPException(status_code=404)
    return dish


# Delete
@v1.delete("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
async def delete_dish(
    submenu_id: Annotated[int, Path(title="Submenu ID", ge=1)],
    dish_id: Annotated[int, Path(title="Submenu ID", ge=1)],
):
    result = await Dish.delte_dish(to_submenu=submenu_id, id=dish_id)
    if not result:
        raise HTTPException(status_code=404)
    return {"ok": result}
