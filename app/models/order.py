from sqlalchemy import Column, Integer, ForeignKey, Numeric, Enum
from app.database.database import Base
from app.enums.order import OrderStatus

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total_amount = Column(Numeric(10,2), nullable=False)
    status = Column(Enum(OrderStatus),nullable=False,default=OrderStatus.PENDING)