import bcrypt
from fastapi import Request, Depends
from sqlmodel import Session

from database import get_db
from models import User

class NotLoggedIn(Exception):
    pass

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def get_optional_user(request: Request, db: Session = Depends(get_db)):
    user_id=request.session.get("user_id")
    if not user_id:
        return None
    return db.get(User, user_id)

def get_current_user(user=Depends(get_optional_user)):
    if not user:
        raise NotLoggedIn()
    return user
