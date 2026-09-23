from enum import Enum

class PaymentStatus(Enum):

    PENDING = "pending"
    PROCESSING = "processing"
    SUCCESSFUL = "successful"
    FAILED = "failed"
    CANCELLED = "cancelled"
    INVALID = "invalid"

class PaymentMethod(Enum):

    MOMO = "momo"
    CARD = "card"
    COD = "cod"