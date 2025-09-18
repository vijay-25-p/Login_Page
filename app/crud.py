from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db_user.id
    return db_user

def signin_user(db: Session, email: str, password: str):
    return db.query(models.User).filter(
        models.User.email == email,
        models.User.password == password
    ).first()
