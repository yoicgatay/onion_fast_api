import pytest
from typing import List
from app.domain.models import User
from app.domain.interfaces import IUserRepository
from app.services.user_service import UserService

class MockUserRepository(IUserRepository):
    def __init__(self):
        self.users = [
            User(id=1, name="Test User 1"),
            User(id=2, name="Test User 2")
        ]

    def get_all(self) -> List[User]:
        return self.users

    def get_by_id(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        raise ValueError(f"User with id {user_id} not found")

@pytest.fixture
def user_repository():
    return MockUserRepository()

@pytest.fixture
def user_service(user_repository):
    return UserService(user_repository)

def test_list_users(user_service):
    users = user_service.list_users()
    assert len(users) == 2
    assert users[0].id == 1
    assert users[0].name == "Test User 1"
    assert users[1].id == 2
    assert users[1].name == "Test User 2"

def test_get_user(user_service):
    user = user_service.get_user(1)
    assert user.id == 1
    assert user.name == "Test User 1"

def test_get_user_not_found(user_service):
    with pytest.raises(ValueError, match="User with id 999 not found"):
        user_service.get_user(999) 