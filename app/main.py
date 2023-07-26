from fastapi import Depends, FastAPI, HTTPException, Path
from database.database import create_data_base
app = FastAPI()
v1 = FastAPI()

from .menu import (
    create_new_menu,
    delete_menu,
    get_menu,
    get_menus,
    update_menu,
)
from .submenu import (
    create_new_submenu,
    get_all_submenu,
    get_submenu,
    update_submenu,
    delete_submenu,
)

from .dish import (
    create_new_dish,
    get_all_dishes,
    get_dish,
    update_dish,
    delete_dish,
)

app.mount("/api/v1", v1)

@app.on_event("startup")
async def database():
    create_data_base()