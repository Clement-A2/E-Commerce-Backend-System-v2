from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from app.enums.payment import PaymentMethod, PaymentStatus

class PaymentCreate(BaseModel):
    order_id: int
    amount: Decimal
    method: PaymentMethod

class PaymentResponse(BaseModel):
    id: int
    order_id: int
    amount: Decimal
    status: PaymentStatus
    method: PaymentMethod

    model_config = ConfigDict(from_attributes=True)