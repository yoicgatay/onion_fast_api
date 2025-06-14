from typing import List
from app.domain.models import User
from app.domain.interfaces import IUserRepository

class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def list_users(self) -> List[User]:
        return self.user_repo.get_all()

    def get_user(self, user_id: int) -> User:
        return self.user_repo.get_by_id(user_id)
