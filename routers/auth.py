from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import logging

from database import get_db
from models.user import User
from schemas.user import UserRegisterRequest
from security import hash_password, verify_password, create_access_token

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/register")
def register(user: UserRegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        logger.warning(f"Attempted duplicate registration: {user.email}")
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)

    new_user = User(
        email=user.email,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    logger.info(f"New user registered: {user.email}")

    return {"message": "User registered successfully"}


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user:
        logger.warning(f"Failed login attempt for {form_data.username}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(form_data.password, user.hashed_password):
        logger.warning(f"Failed login attempt for {form_data.username}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": str(user.id)}
    )

    logger.info(f"User logged in successfully: {user.email}")

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }