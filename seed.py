from sqlmodel import Session, select
from database import engine, init_db
from models import Product

init_db()

PRODUCTS = [
    Product(name="Minimalist Ceramic Mug", description="Handcrafted ceramic mug in matte chalk white.", price=24.0, image="ceramic-mug.jpg", stock=25),
    Product(name="Wireless Matte Headphones", description="Over-ear wireless headphones with a matte black finish.", price=149.0, image="headphones.jpg", stock=15),
    Product(name="Nordic Linen Throw Blanket", description="Soft natural linen throw with a textured weave.", price=68.0, image="linen-throw.jpg", stock=20),
    Product(name="Anodized Desk Lamp", description="Graphite aluminum desk lamp with a slim adjustable arm.", price=92.0, image="desk-lamp.jpg", stock=12),
    Product(name="Ergonomic Mechanical Keyboard", description="Low-profile mechanical keyboard with warm backlighting.", price=135.0, image="keyboard.jpg", stock=10),
    Product(name="Handcrafted Stoneware Vase", description="Speckled stoneware vase with an organic shape.", price=42.0, image="stoneware-vase.jpg", stock=18),
    Product(name="Insulated Travel Tumbler", description="Double-walled stainless steel tumbler that keeps drinks hot or cold.", price=36.0, image="travel-tumbler.jpg", stock=30),
    Product(name="Organic Cotton Tote", description="Heavyweight unbleached cotton canvas tote bag.", price=28.0, image="cotton-tote.jpg", stock=40),

]

with Session(engine) as db:
    if db.exec(select(Product)).first():
        print("Products already exist, skipping.")

    else: 
        db.add_all(PRODUCTS)
        db.commit()
        print("Added {len(PRODUCTS)} products.")

    for p in db.exec(select(Product)).all():
        print (p.id, p.name, p.price, p.image)



