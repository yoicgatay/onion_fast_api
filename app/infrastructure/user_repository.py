from typing import List
from app.domain.models import User
from app.domain.interfaces import IUserRepository

# モック実装
class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self.users = [
            User(id=1, name="Alice"),
            User(id=2, name="Bob"),
        ]

    def get_all(self) -> List[User]:
        return self.users

    def get_by_id(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        raise ValueError("User not found")
