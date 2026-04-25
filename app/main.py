import psycopg2

from fastapi import FastAPI
from app.models import Product
import time
from psycopg2.extras import RealDictCursor





app=FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host='localhost', 
            database='my first project', 
            user='postgres', 
            password='1234',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection successful")
        break
    except Exception as error:
        print('Database connection failed', error)
        time.sleep(2)
    



@app.get("/")
def home():   
    return "Welcome to FastApi"

@app.get("/products")
def get_all_product():
    cursor.execute(""" SELECT * FROM product """)
    data = cursor.fetchall()

    return {'data': data}
 


products=[
    Product(id=1,name="shirt",description="new and premum",price=20.0,quantity=5),
    Product(id= 2,name="pant",description="new and premum",price=20.0,quantity=5),
    Product(id= 3,name="shoe",description="new and premum",price=20.0,quantity=5)
]

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id==id:
            return product
    return "Product not found"



@app.post("/product")
def add_product(product:Product):
    products.append(product)
    return product

    

@app.put("/product/{id}")
def update_product_by_id(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return "Product Update Successful"
    return "No product Found"
        
            

@app.delete("/product")
def delete_product_by_id(id:int,):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "Product delete successful"
    return "Product not found"