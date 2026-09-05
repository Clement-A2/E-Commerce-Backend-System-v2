from pydantic import BaseModel, ConfigDict

class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int
    unit_price: float
    quantity: int

class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    product_id: int
    unit_price: float
    quantity: int

    model_config = ConfigDict(from_attributes=True)