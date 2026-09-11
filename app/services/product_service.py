from app.schemas.product import ProductCreate,ProductResponse
from sqlalchemy.orm import Session
from app.models.product import Product
from app.exceptions.product import (
    ProductNotFoundError
)

class ProductService:

    def create_product(self,db:Session,data:ProductCreate):

        product = Product(
            name= data.name,
            description= data.description,
            price= data.price,
            category_id= data.category_id,
            stock_quantity= data.stock_quantity
        )
        
        db.add(product)
        db.commit()
        db.refresh(product)

        return product

    def get_product(self, db:Session, product_id=int):
        existing_product = db.query(Product).get(product_id)

        if existing_product is None:
            raise ProductNotFoundError("Product was not found/does not exist..!!")

        return existing_product

    def update_product(self, db:Session, product_id:int, data:ProductCreate):
        existing_product = self.get_product(db,product_id)

        existing_product.name = data.name
        existing_product.description = data.description
        existing_product.price = data.price
        existing_product.category_id = data.category_id
        existing_product.stock_quantity = data.stock_quantity

        db.commit()
        db.refresh(existing_product)

        return existing_product

    def delete_product(self, db:Session, product_id:int):
        existing_product = self.get_product(db, product_id)

        db.delete(existing_product)
        db.commit()
        return "Product Deleted Successfully..!!\n"

    def get_all_products(self, db:Session):
        products = db.query(Product).all()

        if not products:
            raise ProductNotFoundError("Products Not Found...!!\n")

        return products