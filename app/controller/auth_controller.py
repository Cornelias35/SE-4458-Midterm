from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.services.auth_service import authenticate_user, get_user, create_user
from app.utils.jwt_handler import create_access_token
from app.models.user import Token, UserOut, User
from app.database.session import SessionLocal
router = APIRouter(
    prefix="/v1/auth",
    tags=["auth"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
async def register(user_data: User, db: Session = Depends(get_db)):
    existing_user = get_user(db, user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    user = create_user(db, user_data.username, user_data.password)
    return UserOut(username=user.username)

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}