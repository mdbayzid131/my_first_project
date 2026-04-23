from fastapi import FastAPI
from models import Product

app=FastAPI()
@app.get("/")
def home():   
    return "Welcome to FastApi"

@app.get("/products")
def get_all_product():
    return products



products=[
    Product(id=1,name="shirt",description="new and premum",price=20.0,quantity=5),
    Product(id= 2,name="pant",description="new and premum",price=20.0,quantity=5),
    Product(id= 3,name="shoe",description="new and premum",price=20.0,quantity=5)
]

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for Product in products:
        if Product.id==id:
            return Product
    return "Product not found"



@app.post("/product")
def add_prouct(product:Product):
    products.append(product)
    return product

    