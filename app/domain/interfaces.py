from abc import ABC, abstractmethod
from typing import List
from .models import User

class IUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        pass 