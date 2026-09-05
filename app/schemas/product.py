from pydantic import BaseModel, ConfigDict

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int
    stock_quantity: int

class ProductResponse(BaseModel):
    id:int
    name: str
    description: str
    price: float
    category_id: int
    stock_quantity: int

    model_config = ConfigDict(from_attributes=True)