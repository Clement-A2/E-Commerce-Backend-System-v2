from app.schemas.cart import CartCreate
from app.database.database import SessionLocal
from app.services.cart_service import CartService
from app.exceptions.cart import (
    CartAlreadyExistsError,
    CartNotFoundError
)

db = SessionLocal()
cart_service = CartService()

data1 = CartCreate(
    user_id=3
)

data2 = CartCreate(
    user_id=4
)

try: 
    result0 = cart_service.create_cart(db,data2)
    print(result0)
    print("Cart Created Successfully...!!\n")
except CartNotFoundError as error:
    print("Caught custom exception:")
    print(error)
except CartAlreadyExistsError as error:
    print("Caught custom exception:")
    print(error)

# try:
#     result1 = cart_service.create_cart(db,data1)
#     print(result1)
#     print("Cart Created Successfully...!!\n")
# except CartNotFoundError as error:
#     print("Caught custom exception:")
#     print(error)
# except CartAlreadyExistsError as error:
#     print("Caught custom exception:")
#     print(error)

# try:
#     result2 = cart_service.get_cart(db, 1)
#     print(result2)
# except CartNotFoundError as error:
#     print("Caught custom exception:")
#     print(error)

# try:
#     result3 = cart_service.get_cart(db, 2)
#     print(result3)
# except CartNotFoundError as error:
#     print("Caught custom exception:")
#     print(error)

try:
    result4 = cart_service.update_cart(db,2,data1)
    print(result4)
    print("Cart Update Successful...!!\n")
except CartNotFoundError as error:
    print("Caught custom exception:")
    print(error)
except CartAlreadyExistsError as error:
    print("Caught custom exception:")
    print(error)

try:
    result5 = cart_service.delete_cart(db,2)
    print(result5)
except CartNotFoundError as error:
    print("Caught custom exception:")
    print(error)

try:
    result5 = cart_service.delete_cart(db,3)
    print(result5)
except CartNotFoundError as error:
    print("Caught custom exception:")
    print(error)

try:
    result6 = cart_service.get_all_carts(db)
    print(result6)
except CartNotFoundError as error:
    print("Caught custom exception:")
    print(error)