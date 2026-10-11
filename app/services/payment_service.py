from app.schemas.payment import PaymentCreate, PaymentResponse
from app.models.payment import Payment
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.exceptions.payment import (
    PaymentFailedError,
    PaymentInProcessingError,
    PaymentNotFoundError,
    InvalidPaymentError,
    InvalidPaymentMethodError,
    InsufficientPaymentAmountError
)
from app.services.order_service import OrderService
from app.enums.payment import PaymentStatus, PaymentMethod
from app.services.order_service import OrderService
from app.enums.order import OrderStatus

class PaymentService:

    def create_payment(self, db: Session, data: PaymentCreate):

        order_service = OrderService()

        order = order_service.get_order(db, data.order_id)

        if order.status ==  OrderStatus.COMPLETED:
            raise InvalidPaymentError("Cannot Make Payment For A Completed Order....!!!")

        if data.amount < order.total_amount:
            raise InsufficientPaymentAmountError("Payment Amount Should Not Be Less Than The Total Order Amount...!!")

        found_payment = db.query(Payment).filter(and_(Payment.order_id == data.order_id), Payment.status.in_([PaymentStatus.PENDING, PaymentStatus.PROCESSING, PaymentStatus.SUCCESSFUL])).first()

        if found_payment:
            raise PaymentInProcessingError("Payment For The Order Already In Processing or Is Pending or Is Completed Successfully...!!")

        payment = Payment(
            order_id= data.order_id,
            amount= data.amount,
            method= data.method
        )

        db.add(payment)
        db.commit()
        db.refresh(payment)

        return payment

    def get_payment(self, db: Session, payment_id: int):

        found_payment = db.query(Payment).get(payment_id)

        if not found_payment:
            raise PaymentNotFoundError("Payment Not Found In Records...!!")

        return found_payment

    def get_order_payments(self, db: Session, order_id: int):

        order_service = OrderService()

        found_order = order_service.get_order(db,order_id)

        found_payments = db.query(Payment).filter(Payment.order_id == order_id).all()

        if not found_payments:
            raise PaymentNotFoundError("No Payments Found For The Particular Order...!!")

        return found_payments

    def update_payment(self, db: Session, payment_id: int, status: PaymentStatus):

        found_payment = self.get_payment(db, payment_id)

        found_payment.status = status

        db.commit()
        db.refresh(found_payment)

        return found_payment

    def cancel_payment(self, db: Session, payment_id: int):

        found_payment = self.get_payment(db, payment_id)

        found_payment.status = PaymentStatus.CANCELLED

        db.commit()
        db.refresh(found_payment)

        return found_payment
    
    def process_successful_payment(self, db: Session, payment_id: int):

        found_payment = self.get_payment(db, payment_id)

        if found_payment.status != PaymentStatus.PROCESSING:
            raise InvalidPaymentError("Payment Is Not In Processing State...!!")

        found_payment.status = PaymentStatus.SUCCESSFUL

        order_service = OrderService()

        order = order_service.get_order(db, found_payment.order_id)

        order.status = OrderStatus.COMPLETED

        db.commit()
        db.refresh(found_payment)
        db.refresh(order)

        return found_payment, order