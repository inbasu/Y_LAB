from fastapi.testclient import TestClient
from app.main import v1

URL = ""
client = TestClient(v1)

menu = {
    "title": "My menu 0",
    "description": "My menu description 0",
}
submenu = {"title": "My submenu 1", "description": "My submenu description 1"}


updated_submenu = {
    "title": "My updated submenu 1",
    "description": "My updated submenu description 1",
}


def test_create_menu():
    response = client.post("/menus", json=menu)
    assert response.status_code == 201, " Wrong status code"
    response = response.json()
    assert response["id"] == 2, "Wrong id"
    assert response["title"] == menu["title"], "Wrong title"
    assert response["description"] == menu["description"], "Wrong description"


def test_get_empty_submemenus():
    response = client.get("/menus/2/submenus")
    assert response.status_code == 200, " Wrong status code"
    assert response.json() == []


def test_create_submenu():
    response = client.post("/menus/2/submenus", json=submenu)
    assert response.status_code == 201, " Wrong status code"
    response = response.json()
    assert response["id"] == 1, "Wrong id"
    assert response["title"] == submenu["title"], "Wrong title"
    assert response["description"] == submenu["description"], "Wrong description"


def test_get_new_submenu():
    response = client.get("/menus/2/submenus/1")
    assert response.status_code == 200, " Wrong status code"
    response = response.json()
    assert response["id"] == 1
    assert response["title"] == submenu["title"], "Wrong title"
    assert response["description"] == submenu["description"], "Wrong description"


def test_get_submenus():
    response = client.get("/menus/2/submenus")
    assert response.status_code == 200, " Wrong status code"
    response = response.json()
    assert response != [], "Menu list not empty"


def test_update_submenu():
    response = client.patch("/menus/2/submenus/1", json=updated_submenu)
    assert response.status_code == 200, " Wrong status code"
    response = response.json()
    assert response["id"] == 1
    assert response["title"] == updated_submenu["title"], "Wrong title"
    assert (
        response["description"] == updated_submenu["description"]
    ), "Wrong description"


def test_get_updated_submenu():
    response = client.get("/menus/2/submenus/1")
    assert response.status_code == 200, " Wrong status code"
    response = response.json()
    assert response["id"] == 1
    assert response["title"] == updated_submenu["title"], "Wrong title"
    assert (
        response["description"] == updated_submenu["description"]
    ), "Wrong description"


def test_delete_submenu():
    response = client.delete("/menus/2/submenus/1")
    assert response.status_code == 200, " Wrong status code"


def test_get_deleted_submemenus():
    response = client.get("/menus/2/submenus")
    assert response.status_code == 200, " Wrong status code"
    assert response.json() == []


def test_get_deleted_submenu():
    response = client.get("/menus/2/submenus/1")
    assert response.status_code == 404, " Wrong status code"
    response = response.json()
    assert response["detail"] == "submenu not found", "Item not delete"


def test_deleted_menu():
    response = client.delete("/menus/2")
    assert response.status_code == 200, " Wrong status code"


def test_get_deleted_menus():
    response = client.get("/menus")
    assert response.status_code == 200, " Wrong status code"
    assert response.json() == []
