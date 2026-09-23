class PaymentNotFoundError(Exception):
    pass

class PaymentInProcessingError(Exception):
    pass

class PaymentFailedError(Exception):
    pass

class InvalidPaymentError(Exception):
    pass

class InvalidPaymentMethodError(Exception):
    pass

class InsufficientPaymentAmountError(Exception):
    pass