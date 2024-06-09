from .schemas import UserCreate, UserBase
from database import get_db
from fastapi import Depends, APIRouter, HTTPException
from .models import User
from sqlalchemy.orm import Session

user_router = APIRouter()



@user_router.post("/users/", response_model=UserBase)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = User(fname=user.fname, email=user.email, paswword=user.password, login=user.login)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
