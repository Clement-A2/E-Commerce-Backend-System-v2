from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from app.database.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)