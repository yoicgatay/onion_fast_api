from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.domain.models import User
from app.infrastructure.user_repository import InMemoryUserRepository
from app.services.user_service import UserService

router = APIRouter()

# DIコンテナのような簡易実装
def get_user_service() -> UserService:
    repo = InMemoryUserRepository()
    return UserService(user_repo=repo)

@router.get("/users", response_model=List[User])
def list_users(service: UserService = Depends(get_user_service)):
    return service.list_users()

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    try:
        return service.get_user(user_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")
