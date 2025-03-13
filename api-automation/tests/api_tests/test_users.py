import pytest
from utils import api_utils

# Example using pytest.mark to group tests
@pytest.mark.users
def test_create_user():
    user_data = {"name": "Test User", "email": "test@example.com"}
    response = api_utils.post("/users", data=user_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"
    assert "id" in response.json()

@pytest.mark.users
def test_get_user():
    response = api_utils.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

@pytest.mark.users
def test_update_user():
    updated_data = {"name": "Updated User"}
    response = api_utils.put("/users/1", data=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"

@pytest.mark.users
def test_delete_user():
    response = api_utils.delete("/users/1")
    assert response.status_code == 200

@pytest.mark.users
def test_get_all_users():
    response = api_utils.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0