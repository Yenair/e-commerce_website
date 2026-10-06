from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from sqlmodel import Session, select

from database import get_db
from models import User
from auth import hash_password, verify_password, get_optional_user
from templating import templates

router = APIRouter()

@router.get("/register")
def register_page(request: Request, user=Depends(get_optional_user)):
    if user:
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse(
        request, "register.html", {"user": None, "error": None}
    )

@router.post("/register")
def register (
    request: Request,
    email:str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    email = email.strip().lower()

    error =None 
    if len(password) <6:
        error = "Password must be at least 6 characters."
    elif len(password.encode()) >72:
        error = "Password is too long."
    elif db.exec(select(User).where(User.email == email)).first():
        error = "That email is already registered."

    if error:
        return templates.TemplateResponse(
            request, "login.html", {"user": None, "error":None}
        )

    user = User(email=email, password_hash = hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)

    request.session["user_id"] = user.id
    return RedirectResponse("/", status_code=303)

@router.get("/login")
def login_page(request: Request, user =Depends (get_optional_user)):
    if user:
        return RedirectResponse("/", ststus_code=303)
    return templates.TemplateResponse(
        request, "login.html", {"user": None, "error": None}
    )

@router.post("/login")
def login(
    request: Request,
    email: str =Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    email = email.strip().lower()
    user = db.exec(select(User).where(User.email == email)).first()

    if not user or not verify_password(password, user.password_hash):
        return templates.TemplateResponse(
            request, 
            "login.html",
            {"User": None, "error": "Wrong email or password."},
            status_code=400,
        )
    request.session["user_id"] = user.id
    return RedirectResponse("/", status_code=303)

@router.post("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)
