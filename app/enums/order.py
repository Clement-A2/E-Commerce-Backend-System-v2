from enum import Enum

class OrderStatus(Enum):
    PENDING="pending"
    PROCESSING="processing"
    COMPLETED="completed"
    FAILED="failed"