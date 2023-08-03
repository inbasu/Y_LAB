from fastapi import Depends, FastAPI, HTTPException, Path

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
    get_submenus,
    get_submenu,
    update_submenu,
    delete_submenu,
)

from .dish import (
    create_new_dish,
    get_dishes,
    get_dish,
    update_dish,
    delete_dish,
)

app.mount("/api/v1", v1)
