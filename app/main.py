from  fastapi import FastAPI, Depends, HTTPException, status
from .models import Products as ProductModel
from sqlalchemy.orm import Session
from .database import engine, get_db
from . import models, schemas

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

    



@app.get("/products", )
def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductModel).all()
    return products
 


@app.get("/product/{id}", response_model=schemas.Product)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@app.post("/product", status_code=status.HTTP_201_CREATED, response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = ProductModel(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.put("/product/{id}", response_model=schemas.Product)
def update_product(id: int, updated_product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product_query = db.query(ProductModel).filter(ProductModel.id == id)
    product = product_query.first()
    
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    product_query.update(updated_product.model_dump(), synchronize_session=False)
    db.commit()
    return product_query.first()

@app.delete("/product/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db)):
    product_query = db.query(ProductModel).filter(ProductModel.id == id)
    product = product_query.first()

    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    product_query.delete(synchronize_session=False)
    db.commit()
    return None



