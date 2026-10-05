from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: Optional[int] = Field (default = None, primary_key=True)
    email:str = Field(unique=True, index=True)
    password_hash: str

class Product(SQLModel, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    name:str
    description: str = ""
    price: float
    image: str = "placeholder.jpg"
    stock: int =10