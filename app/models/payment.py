from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, Enum
from app.database.database import Base
from app.enums.payment import PaymentMethod,PaymentStatus

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.PENDING)
    method = Column(Enum(PaymentMethod))