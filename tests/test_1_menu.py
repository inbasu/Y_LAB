from fastapi.testclient import TestClient
from httpx import Response

from app.main import v1

URL = ''
client = TestClient(v1)

menu = {
    'title': 'My menu 0',
    'description': 'My menu description 0',
}
updated_menu = {
    'title': 'My updated menu 1',
    'description': 'My updated menu description 1',
}


def test_get_empty_menus() -> None:
    response: Response = client.get('/menus')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() == [], 'Menu list not empty'


def test_create_menu() -> None:
    response: Response = client.post('/menus', json=menu)
    assert response.status_code == 201, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1, 'Wrong id'
    assert data['title'] == menu['title'], 'Wrong title'
    assert data['description'] == menu['description'], 'Wrong description'


def test_get_new_menu() -> None:
    response: Response = client.get('/menus/1')
    assert response.status_code == 200, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1
    assert data['title'] == menu['title'], 'Wrong title'
    assert data['description'] == menu['description'], 'Wrong description'


def test_get_menus() -> None:
    response: Response = client.get('/menus')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() != [], 'Menu list not empty'


def test_update_menu() -> None:
    response: Response = client.patch('/menus/1', json=updated_menu)
    assert response.status_code == 200, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1
    assert data['title'] == updated_menu['title'], 'Wrong title'
    assert data['description'] == updated_menu['description'], 'Wrong description'


def test_get_updated_menu() -> None:
    response: Response = client.get('/menus/1')
    assert response.status_code == 200, ' Wrong status code'
    data = response.json()
    assert data['id'] == 1
    assert data['title'] == updated_menu['title'], 'Wrong title'
    assert data['description'] == updated_menu['description'], 'Wrong description'


def test_deleted_menu() -> None:
    response: Response = client.delete('/menus/1')
    assert response.status_code == 200, ' Wrong status code'


def test_get_deleted_menus() -> None:
    response: Response = client.get('/menus')
    assert response.status_code == 200, ' Wrong status code'
    assert response.json() == []


def test_get_deleted_menu() -> None:
    response: Response = client.get('/menus/1')
    assert response.status_code == 404, ' Wrong status code'
    data = response.json()
    assert data['detail'] == 'menu not found', 'Item not delete'
