from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

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

class CartItem(SQLModel, table=True):
    id: Optional[int] =Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    product_id: int = Field(foreign_key = "product.id")
    quantity: int =1
    product: Optional[Product] = Relationship()

