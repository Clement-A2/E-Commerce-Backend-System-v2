from app.schemas.product import ProductCreate
from app.services.product_service import ProductService
from app.database.database import SessionLocal

data = ProductCreate(
    name="Laptop",
    description="Gaming Laptop",
    price=5000,
    category_id=1,
    stock_quantity=10
)

product_service = ProductService()
db=SessionLocal()

# result = product_service.create_product(db,data)
# print(result)

# product = product_service.get_product(db,result.id)
# print(product.id)
# print(product.name)
# print(product.price)
# print(product.category_id)
# print(product.stock_quantity)

# updated_data = ProductCreate(
#     name = "Desktop PC",
#     description= "Workstation Device",
#     price= 2300,
#     category_id=1,
#     stock_quantity= 15
# )

# updated_product_service = ProductService()

# update_product = updated_product_service.update_product(db,result.id,updated_data)
# print(update_product)

# product2 = updated_product_service.get_product(db,update_product.id)
# print(product2.id)
# print(product2.name)
# print(product2.price)
# print(product2.category_id)
# print(product2.stock_quantity)

products = product_service.get_all_products(db)
print(products)

# product_id = products[1].id

# result = product_service.delete_product(db,product_id)
# print(result)