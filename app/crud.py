from sqlalchemy.orm import Session
from . import models, schemas
from bcrypt import hashpw, gensalt, checkpw

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hashpw(user.password.encode('utf-8'), gensalt())
    db_user = models.User(
        user_name=user.user_name,
        email=user.email,
        hashed_password=hashed_password.decode('utf-8')
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def login_user(db: Session, email: str, password: str):
    db_user = get_user_by_email(db, email=email)
    if db_user and checkpw(password.encode('utf-8'), db_user.hashed_password.encode('utf-8')):
        return db_user
    return None

