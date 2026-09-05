from pydantic import BaseModel, ConfigDict

class PaymentCreate(BaseModel):
    order_id: int
    amount: float
    method: str

class PaymentResponse(BaseModel):
    id: int
    order_id: int
    amount: float
    status: str
    method: str

    model_config = ConfigDict(from_attributes=True)