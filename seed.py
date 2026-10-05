from sqlmodel import Session, select
from database import engine, init_db
from models import Product

init_db()

with Session(engine) as db:
    existing = db.exec(select(Product)).first()
    if existing:
        print("Products already exist, skipping.")

    else: 
        db.add_all([
            Product(name="Classic Sneakers", description="Confortable foot wear", price=100000),
            Product(name="Leather Wallet", description="Slim Black Wallet", price=50000),
            Product(name="Backpack", description="Fits a 1-inch laptop", price=60000)
        ])
        db.commit()
        print("Added 3 products.")

    for p in db.exec(select(Product)).all():
        print (p.id, p.name, p.price)



