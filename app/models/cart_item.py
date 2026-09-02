from sqlalchemy import Column, Integer, ForeignKey
from app.database.database import Base

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"), index=True, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), index=True, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)