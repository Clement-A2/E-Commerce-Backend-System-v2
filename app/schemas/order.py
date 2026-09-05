from pydantic import BaseModel, ConfigDict

class OrderCreate(BaseModel):
    user_id: int
    total_amount: float

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_ammount: float
    status: str

    model_config = ConfigDict(from_attributes=True)