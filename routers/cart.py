from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlmodel import Session, select


from models import CartItem, Product
from auth import get_current_user
from templating import templates
from database import get_db

router = APIRouter(prefix="/cart")

@router.get("")
def view_cart(
    request:Request,
    user=Depends(get_current_user),
    db: Session = Depends(get_db),
): 
    items = db.exec(select(CartItem).where(CartItem.user_id == user.id)).all()
    total = sum(item.product.price * item.quantity for item in items)
    return templates.TemplateResponse(
        request, "cart.html", {"items": items, "total": total, "user": user}
    )

@router.post("/add/{product_id}")
def add_to_cart(
    product_id: int,
    quantity: int = Form(1),
    user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail = "Product not found")

    if product.stock <=0:
        return RedirectResponse(f"/products/{product_id}", status_code=303)

    quantity = max(1, quantity)

    item = db.exec(
        select(CartItem).where(
            CartItem.user_id == user.id, CartItem.product_id == product_id
        )
    ).first()

    current = item.quantity if item else 0
    total_requested = current + quantity

    if total_requested > product.stock:
        new_quantity = product.stock
    else:
        new_quantity = total_requested

    if item:
        item.quantity = new_quantity
    else:
        db.add(CartItem(user_id=user.id, product_id=product_id, quantity=new_quantity))

    db.commit()
    return RedirectResponse("/cart", status_code=303)

@router.post("/update/{item_id}")
def update_cart_item(
    item_id: int,
    quantity: int = Form(...),
    user=Depends (get_current_user),
    db: Session = Depends(get_db),
):
    item = db.get(CartItem, item_id)

    if item and item.user_id == user.id:
        if quantity<=0:
            db.delete(item)
        else:
            item.quantity = min(quantity, item.product.stock)
        db.commit()
    return RedirectResponse("/cart", status_code=303)


@router.post("/remove/{item_id}")
def remove_cart_item(
    item_id: int,
    user= Depends(get_current_user),
    db: Session = Depends(get_db),
): 
    item = db.get(CartItem, item_id)

    if item and item.user_id == user.id:
        db.delete(item)
        db.commit()

    return RedirectResponse("/cart", status_code=303)