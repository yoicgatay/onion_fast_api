import pytest
from fastapi.testclient import TestClient
from app.domain.models import User
from app.domain.interfaces import IUserRepository
from app.services.user_service import UserService
from app.api.user_router import router, get_user_service
from fastapi import FastAPI

class MockUserRepository(IUserRepository):
    def __init__(self):
        self.users = [
            User(id=1, name="Test User 1"),
            User(id=2, name="Test User 2")
        ]

    def get_all(self) -> list[User]:
        return self.users

    def get_by_id(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        raise ValueError(f"User with id {user_id} not found")

@pytest.fixture
def client():
    app = FastAPI()
    mock_repo = MockUserRepository()
    
    # Override the get_user_service dependency
    def override_get_user_service():
        return UserService(user_repo=mock_repo)
    
    app.include_router(router)
    # Override the dependency with our mock version
    app.dependency_overrides[get_user_service] = override_get_user_service
    return TestClient(app)

def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 2
    assert users[0]["id"] == 1
    assert users[0]["name"] == "Test User 1"
    assert users[1]["id"] == 2
    assert users[1]["name"] == "Test User 2"

def test_get_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert user["name"] == "Test User 1"

def test_get_user_not_found(client):
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found" 