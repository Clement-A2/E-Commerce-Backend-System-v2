from pydantic import BaseModel, ConfigDict

class CartCreate(BaseModel):
    user_id: int

class CartResponse(BaseModel):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)