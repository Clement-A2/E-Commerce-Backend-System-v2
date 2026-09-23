from app.schemas.order import OrderCreate
from app.services.order_service import OrderService
from app.database.database import SessionLocal
from app.exceptions.order import (
    OrderAlreadyExistsError,
    OrderNotFoundError,
    IncompleteOrderError
)

db = SessionLocal()
order_service = OrderService()

data1 = OrderCreate(
    user_id = 3,
    total_amount= 2000
)

try:
    result1 = order_service.create_order(db,data1)
    print(result1)
except OrderAlreadyExistsError as error:
    print("Caught custom exception:")
    print(error)

try:
    result2 = order_service.get_order(db, 1)
    print(result2.id)
    print(result2.user_id)
    print(result2.total_amount)
    print(result2.status)
    # result3 = order_service.get_all_orders(db)
    # print(result3)
except OrderNotFoundError as error:
    print("Caught custom exception:")
    print(error)