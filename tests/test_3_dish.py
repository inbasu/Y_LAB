from fastapi.testclient import TestClient
from httpx import Response

from app.main import v1

URL = ''
client = TestClient(v1)

menu = {
    'title': 'My menu 0',
    'description': 'My menu description 0',
}

submenu = {'title': 'My submenu 1', 'description': 'My submenu description 1'}

dish = {
    'title': 'My dish 1',
    'description': 'My dish description 1',
    'price': 12.50,
}

updated_dish = {
    'title': 'My updated dish 1',
    'description': 'My updated dish description 1',
    'price': 14.50,
}


def test_create_menu() -> None:
    response: Response = client.post('/menus', json=menu)
    assert response.status_code == 201, ' Wrong status code'
    data = response.json()
    assert data['id'] == 3, 'Wrong id'
    assert data['title'] == menu['title'], 'Wrong title'
    assert data['description'] == menu['description'], 'Wrong description'


def test_create_submenu() -> None:
    response: Response = client.post('/menus/3/submenus', json=submenu)
    assert response.status_code == 201, ' Wrong status code'
    data = response.json()
    assert data['id'] == 2, 'Wrong id'
    assert data['title'] == submenu['title'], 'Wrong title'
    assert data['description'] == submenu['description'], 'Wrong description'


def test_get_empty_dishes() -> None:
    response: Response = client.get('/menus/3/submenus/2/dishes')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() == []


def test_create_dish() -> None:
    response: Response = client.post('/menus/3/submenus/2/dishes', json=dish)
    assert response.status_code == 201, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1, 'Wrong id'
    assert data['title'] == dish['title'], 'Wrong title'
    assert data['description'] == dish['description'], 'Wrong description'
    assert data['price'] == dish['price'], 'Wrong price'


def test_get_new_dish() -> None:
    response: Response = client.get('/menus/3/submenus/2/dishes/1')
    assert response.status_code == 200, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1, 'Wrong id'
    assert data['title'] == dish['title'], 'Wrong title'
    assert data['description'] == dish['description'], 'Wrong description'
    assert data['price'] == dish['price'], 'Wrong price'


def test_get_new_dishes() -> None:
    response: Response = client.get('/menus/3/submenus/2/dishes')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() != []


def test_update_dish() -> None:
    response: Response = client.patch('/menus/3/submenus/2/dishes/1', json=updated_dish)
    assert response.status_code == 200, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1
    assert data['title'] == updated_dish['title'], 'Wrong title'
    assert data['description'] == updated_dish['description'], 'Wrong description'
    assert data['price'] == updated_dish['price'], 'Wrong price'


def test_get_updated_dish() -> None:
    response: Response = client.get('/menus/3/submenus/2/dishes/1')
    assert response.status_code == 200, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1
    assert data['title'] == updated_dish['title'], 'Wrong title'
    assert data['description'] == updated_dish['description'], 'Wrong description'
    assert data['price'] == updated_dish['price'], 'Wrong price'


###
def test_delete_dish() -> None:
    response: Response = client.delete('/menus/3/submenus/2/dishes/1')
    assert response.status_code == 200, ' Wrong status code'


def test_get_deleted_dishes() -> None:
    response: Response = client.get('/menus/3/submenus/2/dishes')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() == []


def test_get_deleted_dish() -> None:
    response: Response = client.get('/menus/3/submenus/2/dishes/1')
    assert response.status_code == 404, ' Wrong status code'
    data = response.json()
    assert data['detail'] == 'dish not found', 'Item not delete'


def test_delete_submenu() -> None:
    response: Response = client.delete('/menus/3/submenus/2')
    assert response.status_code == 200, ' Wrong status code'


def test_get_deleted_submemenus() -> None:
    response = client.get('/menus/1/submenus')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() == []


def test_deleted_menu() -> None:
    response: Response = client.delete('/menus/3')
    assert response.status_code == 200, ' Wrong status code'


def test_get_deleted_menus() -> None:
    response: Response = client.get('/menus')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() == []
