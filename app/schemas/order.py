from pydantic import BaseModel, ConfigDict
from app.enums.order import OrderStatus

class OrderCreate(BaseModel):
    user_id: int
    total_amount: float

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: OrderStatus

    model_config = ConfigDict(from_attributes=True)