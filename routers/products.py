from fastapi import APIRouter, Request, Depends, HTTPException
from sqlmodel import Session, select

from database import get_db
from models import Product
from templating import templates

router = APIRouter()

@router.get("/")
def home (request: Request, db: Session = Depends(get_db)):
    products = db.exec (select(Product)).all()
    return templates.TemplateResponse(
        request, "product_list.html", {"products": products}
    )

@router.get ("/products/{product_id}")
def product_detail(product_id:int, request: Request, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return templates.TemplateResponse(
        request, "product_detail.html", {"product":product}
    )

