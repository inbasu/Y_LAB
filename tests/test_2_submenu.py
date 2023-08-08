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


updated_submenu = {
    'title': 'My updated submenu 1',
    'description': 'My updated submenu description 1',
}


def test_create_menu() -> None:
    response: Response = client.post('/menus', json=menu)
    assert response.status_code == 201, ' Wrong status code'
    data = response.json()
    assert data['id'] == 2, 'Wrong id'
    assert data['title'] == menu['title'], 'Wrong title'
    assert data['description'] == menu['description'], 'Wrong description'


def test_get_empty_submemenus() -> None:
    response: Response = client.get('/menus/2/submenus')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() == []


def test_create_submenu() -> None:
    response: Response = client.post('/menus/2/submenus', json=submenu)
    assert response.status_code == 201, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1, 'Wrong id'
    assert data['title'] == submenu['title'], 'Wrong title'
    assert data['description'] == submenu['description'], 'Wrong description'


def test_get_new_submenu() -> None:
    response: Response = client.get('/menus/2/submenus/1')
    assert response.status_code == 200, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1
    assert data['title'] == submenu['title'], 'Wrong title'
    assert data['description'] == submenu['description'], 'Wrong description'


def test_get_submenus() -> None:
    response: Response = client.get('/menus/2/submenus')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() != [], 'Menu list not empty'


def test_update_submenu() -> None:
    response: Response = client.patch('/menus/2/submenus/1', json=updated_submenu)
    assert response.status_code == 200, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1
    assert data['title'] == updated_submenu['title'], 'Wrong title'
    assert (
        data['description'] == updated_submenu['description']
    ), 'Wrong description'


def test_get_updated_submenu() -> None:
    response: Response = client.get('/menus/2/submenus/1')
    assert response.status_code == 200, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1
    assert data['title'] == updated_submenu['title'], 'Wrong title'
    assert (
        data['description'] == updated_submenu['description']
    ), 'Wrong description'


def test_delete_submenu() -> None:
    response: Response = client.delete('/menus/2/submenus/1')
    assert response.status_code == 200, ' Wrong status code'


def test_get_deleted_submemenus() -> None:
    response: Response = client.get('/menus/2/submenus')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() == []


def test_get_deleted_submenu() -> None:
    response: Response = client.get('/menus/2/submenus/1')
    assert response.status_code == 404, ' Wrong status code'
    data = response.json()
    assert data['detail'] == 'submenu not found', 'Item not delete'


def test_deleted_menu() -> None:
    response: Response = client.delete('/menus/2')
    assert response.status_code == 200, ' Wrong status code'


def test_get_deleted_menus() -> None:
    response: Response = client.get('/menus')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() == []
