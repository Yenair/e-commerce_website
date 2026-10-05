from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI() 

class Catergory(BaseModel):
    id:int
    name:str


class Product (BaseModel): 
    price:float
    in_stock:bool = True
    category: Catergory


class OrderItem(BaseModel):
    product_id:int
    quantity:int

class Order(BaseModel):
    customer_name:int
    itsms:list[OrderItem]

@app.post("/order")
def create_order(order:Order):

    return {"mesage": "Order Created Successfully"
            "order":order
            }

@app.get("/")
def read_root():
    return {"message":"Welcome to fast api ...."}

products = [
    {"id":1, "name": "laptop", "price":89000},
    {"id":2, "name": "mobile", "price":89000},
    {"id":3, "name": "food", "price":89000},
]

@app.get("/products")
def get_products():
    return {
        "products":products
    }


def create_product():
    return {
        "message": "product created succesfully"
    }

@app.post("/products")
def create_product():
    return {"message":"Product created successfully"}

@app.put("/product/1")
def update_product():
    return {"message":"product updated successfully"}

@app.delete("/delete/1")
def delete_product():
    return {"message":"product has been deleted successfully"}


@app.get("/products/1")
def get_products_details():
    return {
        "id":1,
        "name":"mobile",
        "price": 799
    }

@app.get("/users/1")
def get_user_details():
    return {
        "is": 1,
        "name": "Zosh",
        "age": 35,
        "adress": {
            "city": "newyork", "state":"new york"
            },
        "orders":[{"id":"order id 1", "products":"mobile"}]
    }

categories = {"mobile": "iphone", "car":"nissan"}

@app.post
def create_category():
    return {"message": "Category has been created successfully"}




@app.get("/categories")
def get_categories ():
    return {
        "categories":categories
    }



