from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from sqlmodel import Session, select, desc

from database import get_db
from models import CartItem, Order, OrderItem
from auth import get_current_user
from templating import templates

router= APIRouter()


@router.post("/checkout")
def checkout(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    items = db.exec(select(CartItem).where(CartItem.user_id == user.id)).all()

    if not items:
        return RedirectResponse("/cart", status_code=303)

    #making sure everything is still in stock
    problem = False
    for item in items:
        available = item.product.stock
        if item.quantity > available:
            problem = True
            if available <=0:
                db.delete(item)
            else:
                item.quantity= available
    if problem:
        db.commit()
        return RedirectResponse("/cart", status_code=303)

    #2. Creating the order
    total = sum(item.product.price *item.quantity for item in items)
    order = Order(user_id=user.id, total=total)
    db.add(order)
    db.flush() #gives the order an id without finishing the transaction

    #3. Copy cart items into items, reduce stock, empty the cart
    for item in items:
        db.add(
            OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.product.price,
            )
        )
        item.product.stock -= item.quantity
        db.delete(item)
    
    #4. Save everything at once
    db.commit()
    return RedirectResponse("/orders?placed={order.id}", status_code=303) 


@router.get("/orders")
def my_orders(
    request: Request,
    user= Depends(get_current_user),
    db: Session = Depends(get_db),
):
    orders = db.exec(
        select(Order).where(Order.user_id == user.id).order_by(desc(Order.created_at))
    ).all()

    placed = request.query_params.get("placed")

    return templates.TemplateResponse(
        request, "orders.html", {"orders":orders, "user": user, "placed": placed}
    )