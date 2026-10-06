from fastapi import APIRouter, Request, Depends, HTTPException
from sqlmodel import Session, select

from database import get_db
from models import Product
from templating import templates
from auth import get_optional_user

router = APIRouter()

@router.get("/")
def home (
    request: Request, 
    db: Session = Depends(get_db), 
    user=Depends(get_optional_user)
    ):

    products = db.exec (select(Product)).all()
    return templates.TemplateResponse(
        request, "product_list.html", {"products": products, "user": user}
    )

@router.get ("/products/{product_id}")
def product_detail(
    product_id:int, 
    request: Request, 
    db: Session = Depends(get_db),
    user= Depends(get_optional_user),
    ):

    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return templates.TemplateResponse(
        request, "product_detail.html", {"product":product, "user": user}
    )

