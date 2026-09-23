from app.database.database import SessionLocal
from app.services.payment_service import PaymentService
from app.services.order_service import OrderService
from app.schemas.payment import PaymentCreate, PaymentResponse
from app.enums.payment import PaymentMethod, PaymentStatus
from app.enums.order import OrderStatus
from app.exceptions.payment import (
    PaymentNotFoundError,
    PaymentInProcessingError
)

db = SessionLocal()
payment_service = PaymentService()

def test_get_payment():

    try:
        data1 = PaymentCreate(
            order_id = 1,
            amount=2000,
            method=PaymentMethod.MOMO
        )

        result1 = payment_service.create_payment(db,data1)
        print(result1.id)
        print(result1.order_id)
        print(result1.amount)
        print(result1.method)
        print("Payment Created Successfully...!!\n")

        payment = payment_service.get_payment(db,result1.id)
        assert payment.id == result1.id
        print(payment)
    except PaymentNotFoundError as error:
        print("Caught custom exception:")
        print(error)
    except PaymentInProcessingError as error:
        print("\nCaught custom exception:")
        print(error)

def test_get_order_payments():

    result2 = payment_service.get_order_payments(db,1)
    print(result2)
    assert result2
    assert result2[0].order_id == 1

def test_update_payment():

    result3 = payment_service.get_order_payments(db,1)[0]

    updated_result3 = payment_service.update_payment(db,result3.id,PaymentStatus.PROCESSING)

    assert updated_result3.status == PaymentStatus.PROCESSING

    print(result3.status)
    print(updated_result3.status)

def test_cancel_payment():

    result4 = payment_service.get_order_payments(db,1)[0]

    cancel_result4 = payment_service.cancel_payment(db,result4.id)

    assert cancel_result4.status == PaymentStatus.CANCELLED

    print(cancel_result4.status)

def test_process_successful_payment():

    # data = PaymentCreate(
    #     order_id=1,
    #     amount=2000,
    #     method=PaymentMethod.MOMO
    # )

    # payment = payment_service.get_payment(db,)
    result = payment_service.update_payment(db, 1,PaymentStatus.PROCESSING)

    successful_payment, order = payment_service.process_successful_payment(db,result.id)

    assert successful_payment.status == PaymentStatus.SUCCESSFUL

    order = OrderService().get_order(db,1)

    assert order.status == OrderStatus.COMPLETED

    print(successful_payment.status)
    print(order.status)

test_process_successful_payment()