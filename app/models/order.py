from sqlalchemy import ForeignKey, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column
from decimal import Decimal
from app.database.database import Base
from app.enums.order import OrderStatus

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus),nullable=False,default=OrderStatus.PENDING)
