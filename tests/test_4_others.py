# from fastapi.testclient import TestClient
# from app.main import v1

# URL = ""
# client = TestClient(v1)

# menu = {
#     "title": "My menu 0",
#     "description": "My menu description 0",
# }

# submenu = {"title": "My submenu 1", "description": "My submenu description 1"}

# dish = {
#     "title": "My dish 1",
#     "description": "My dish description 1",
#     "price": 12.50,
# }

# dish2 = {
#     "title": "My dish 2",
#     "description": "My dish description 2",
#     "price": 12.50,
# }


# def test_create_menu():
#     response = client.post("/menus", json=menu)
#     assert response.status_code == 202, " Wrong status code"
#     response = response.json()
#     assert response["id"] == 4, "Wrong id"
#     assert response["title"] == menu["title"], "Wrong title"
#     assert response["description"] == menu["description"], "Wrong description"


# def test_create_submenu():
#     response = client.post("/menus/4/submenus", json=submenu)
#     assert response.status_code == 201, " Wrong status code"
#     response = response.json()
#     assert response["id"] == 3, "Wrong id"
#     assert response["title"] == submenu["title"], "Wrong title"
#     assert response["description"] == submenu["description"], "Wrong description"


# def test_create_dish():
#     response = client.post("/menus/4/submenus/3/dishes", json=dish)
#     assert response.status_code == 201, " Wrong status code"
#     response = response.json()
#     assert response["id"] == 2, "Wrong id"
#     assert response["title"] == dish["title"], "Wrong title"
#     assert response["description"] == dish["description"], "Wrong description"
#     assert response["price"] == dish["price"], "Wrong price"


# def test_create_dish2():
#     response = client.post("/menus/4/submenus/3/dishes", json=dish2)
#     assert response.status_code == 201, " Wrong status code"
#     response = response.json()
#     assert response["id"] == 3, "Wrong id"
#     assert response["title"] == dish2["title"], "Wrong title"
#     assert response["description"] == dish2["description"], "Wrong description"
#     assert response["price"] == dish2["price"], "Wrong price"


# def test_get_menu():
#     response = client.get("/menus/4")
#     assert response.status_code == 200, " Wrong status code"
#     response = response.json()
#     assert response["id"] == 4
#     assert response["title"] == menu["title"], "Wrong title"
#     assert response["description"] == menu["description"], "Wrong description"
#     assert response["submenus_count"] == 1, "Wrong submenus count"
#     assert response["dishes_count"] == 2, "Wrong dishes count"


# def test_get_submenu():
#     response = client.get("/menus/4/submenus/3")
#     assert response.status_code == 200, " Wrong status code"
#     response = response.json()
#     assert response["id"] == 3
#     assert response["title"] == submenu["title"], "Wrong title"
#     assert response["description"] == submenu["description"], "Wrong description"
#     assert response["dishes_count"] == 2, "Wrong dishes count"


# def test_delete_submenu():
#     response = client.delete("/menus/4/submenus/3")
#     assert response.status_code == 200, " Wrong status code"


# def test_deleted_menu():
#     response = client.delete("/menus/1")
#     assert response.status_code == 200, " Wrong status code"


# def test_get_deleted_submenus():
#     response = client.get("/menus/4/submenus")
#     assert response.status_code == 200, " Wrong status code"
#     assert response.json() == []


# def test_get_deleted_dishes():
#     response = client.get("/menus/4/submenus/3/dishes")
#     assert response.status_code == 200, " Wrong status code"
#     assert response.json() == []


# def test_get_menu_after_deleted_submenus():
#     response = client.get("/menus/4")
#     assert response.status_code == 200, " Wrong status code"
#     response = response.json()
#     assert response["id"] == 4
#     assert response["title"] == menu["title"], "Wrong title"
#     assert response["description"] == menu["description"], "Wrong description"
#     assert response["submenus_count"] == 0, "Wrong submenus count"
#     assert response["dishes_count"] == 0, "Wrong dishes count"


# def test_deleted_menus():
#     response = client.delete("/menus/4")
#     assert response.status_code == 200, " Wrong status code"


# def test_get_deleted_menus():
#     response = client.get("/menus")
#     assert response.status_code == 200, " Wrong status code"
#     assert response.json() == []
