from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()

@router.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.create_user(db, user)
    return {"message": "User registered successfully"}

@router.post("/login")
def login_user(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    db_user = crud.signin_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Invalid email or password" 
        )
    return {"message": "Logged in successfully"}
