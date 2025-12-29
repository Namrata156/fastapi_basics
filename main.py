from fastapi import Depends, FastAPI
from models import Product 
from config import session,engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")

def greet():
    return "Welcome Namrata!"
greet()

products = [
    Product(id=1,name="phone",description="budget phone",price=99,quantity=100),
    Product(id=2,name="laptop",description="gaming laptop",price=1200,quantity=50),
    Product(id=6,name="tablet",description="budget tablet",price=150,quantity=200),
    Product(id=8,name="monitor",description="4k monitor",price=200,quantity=100)
]

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(database_models.Product).count()

    if count==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

        db.commit()

init_db()

@app.get("/products")
def get_all_products(db:Session=Depends(get_db)):

    # db=session()
    #db.query()
    #return db.query(Product).all()
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id:int, db:Session=Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_products:
        return db_products
    return "Product Not Found"
    # for product in products:
    #     if product.id == id:
    #         return product    
    # return "Product Not Found"


@app.post("/product")
def add_product(product:Product, db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/product")
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_products:
        db_products.name=product.name
        db_products.description=product.description
        db_products.price=product.price
        db_products.quantity=product.quantity
        db.commit()
        return "Product updated"
    else:
        return "Product Not Found"
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         products[i]=product
    #     return "Product updated succesfully"

@app.delete("/product")
def delete_product(id:int,db:Session=Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_products:
        db.delete(db_products)
        db.commit()
        return "Product deleted"
    else:
        return "Product Not Found"
    # for i in range(len(products)):
    #     if products[i].id==id:
    #         del products[i]
    #         return "Product deleted"
    # return "Product Not Found"