from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import init_db
import models

@asynccontextmanager
async def lifespan (app: FastAPI):
    init_db()
    yield

app=FastAPI()

@app.get("/")
def home():
    return {"message": "My shop is running"}





