from sqlalchemy import Column, Integer, ForeignKey, Numeric, String
from app.database.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    status = Column(String, nullable=False, default="pending")
    method = Column(String, nullable=False)