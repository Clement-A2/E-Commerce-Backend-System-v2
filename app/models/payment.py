from sqlalchemy import ForeignKey, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column
from decimal import Decimal
from app.database.database import Base
from app.enums.payment import PaymentMethod,PaymentStatus

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    status: Mapped[PaymentStatus] = mapped_column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.PENDING)
    method: Mapped[PaymentMethod] = mapped_column(Enum(PaymentMethod), nullable=False)
