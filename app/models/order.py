from sqlalchemy import Column, Integer, ForeignKey, Numeric, String
from app.database.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total_amount = Column(Numeric(10,2), nullable=False)
    status = Column(String, nullable=False, default="pending")