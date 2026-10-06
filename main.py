from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from auth import NotLoggedIn
from database import init_db
import models
from routers import products, auth_routes, cart

@asynccontextmanager
async def lifespan (app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(SessionMiddleware, secret_key="this is a long hash code")

app.mount("/static", StaticFiles (directory="static"), name="static")
@app.exception_handler(NotLoggedIn)
async def not_logged_in_handler(request: Request, exc: NotLoggedIn):
    return RedirectResponse("/login", status_code=303)

app.include_router(products.router)
app.include_router(auth_routes.router)
app.include_router(cart.router)