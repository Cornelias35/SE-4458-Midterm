from sqlalchemy.orm import Session

from app.models.database_models import UserDB
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, username: str):
    return db.query(UserDB).filter(UserDB.username == username).first()

def create_user(db: Session, username: str, password: str):
    hashed_password = pwd_context.hash(password)
    db_user = UserDB(username=username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user or not pwd_context.verify(password, user.password):
        return None
    return user