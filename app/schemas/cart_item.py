from pydantic import BaseModel, ConfigDict

class CartItemCreate(BaseModel):
    cart_id: int
    product_id: int
    quantity: int

class CartItemResponse(BaseModel):
    id: int
    cart_id: int
    product_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)