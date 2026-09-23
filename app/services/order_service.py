from app.schemas.order import OrderCreate, OrderResponse
from app.models.order import Order
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.exceptions.order import (
    OrderAlreadyExistsError,
    OrderNotFoundError,
    IncompleteOrderError
)
from app.services.user_service import UserService
from app.enums.order import OrderStatus

class OrderService:

    def create_order(self, db: Session,data: OrderCreate):

        user_service = UserService()

        user = user_service.get_user(db, data.user_id)

        existing_order = db.query(Order).filter(and_(Order.user_id == data.user_id, Order.status.in_(["pending", "processing"]))).first()

        if existing_order:
            raise OrderAlreadyExistsError("User Already Has a Pending/Processing Order...!!")

        order = Order(
            user_id = data.user_id,
            total_amount = data.total_amount
        )

        db.add(order)
        db.commit()
        db.refresh(order)

        return order

    def get_order(self, db: Session, order_id: int):

        found_order = db.query(Order).get(order_id)

        if found_order is None:
            raise OrderNotFoundError("Order Not Found in Records...!!")

        return found_order

    def update_order_status(self, db: Session, order_id: int, status: str):
        pass

    def get_all_orders(self, db: Session):

        orders = db.query(Order).all()

        if not orders:
            raise OrderNotFoundError("No Orders Found in Recoreds...!!")

        return orders

    def get_user_orders(self, db: Session, user_id: int):

        user_service = UserService()
        
        user = user_service.get_user(db, user_id)

        found_orders = db.query(Order).filter(Order.user_id == user_id).all()

        if not found_orders:
            raise OrderNotFoundError("No Orders Found for the particular User....!!")

        return found_orders