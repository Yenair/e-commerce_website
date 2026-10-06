from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone

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

class Order(SQLModel , table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    total: float
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    items: List["OrderItem"] = Relationship(back_populates="order")


class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id")
    product_id: int = Field(foreign_key="product.id")
    quantity: int
    price: float
    order: Optional[Order] = Relationship(back_populates="items")
    product: Optional[Product] = Relationship()

