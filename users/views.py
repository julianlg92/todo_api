from dotenv import load_dotenv, find_dotenv
from fastapi import APIRouter, HTTPException, Path
from passlib.context import CryptContext
from starlette import status
from os import environ

from ..database import db_dependency
from .models import User
from .schemas import UserOut, UserBase, UserCreate

router = APIRouter(prefix="/user", tags=["user"])

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

load_dotenv(find_dotenv())
SECRET_KEY = environ["SECRET_KEY"]
ALGORITHM = "HS256"


@router.get("/", response_model=list[UserOut])
async def read_users(db: db_dependency, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


@router.post("/", response_model=UserBase, status_code=status.HTTP_201_CREATED)
async def create_user(
    db: db_dependency,
    user: UserCreate,
):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        **user.model_dump(),
        hashed_password=bcrypt_context.hash(user.password),
    )
    db.add(new_user)
    db.commit()
