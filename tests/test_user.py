import pytest
from api.user_service import UserService


def test_get_user():
    response = UserService.get_user(1)
    assert response.status_code == 200
    assert response.json()["name"] == "Leanne Graham"


def test_get_all_users():
    assert UserService.get_all_users().status_code == 200
    assert len(UserService.get_all_users().json()) > 0


def test_get_invalid_user():
    response = UserService.get_user("x")
    assert response.status_code == 404


def test_create_user():
    new_user_data = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com"
    }
    response = UserService.create_user(new_user_data)
    assert response.status_code == 201


def test_create_duplicate_user():
    new_user_data = {
        "id": 1,
        "name": "Leanne Graham"
    }
    response = UserService.create_user(new_user_data)
    assert response.status_code == 404


def test_update_user():
    updated_data = {
        "name": "Leanne Graham",
        "username": "Brat"
    }
    response = UserService.update_user(1, updated_data)
    assert response.status_code == 200
    assert response.json()["username"] == "Brat"


def test_update_invalid_user():
    updated_data = {
        "name": "Leanne Graham",
        "username": "Brat"
    }
    response = UserService.update_user("x", updated_data)
    assert response.status_code == 404


def test_delete_user():
    response = UserService.delete_user(1)
    assert response.status_code == 200


def test_delete_invalid_user():
    response = UserService.delete_user("x")
    assert response.status_code == 404


def test_get_deleted_user():
    UserService.delete_user(1)
    assert UserService.get_user(1).status_code == 404




