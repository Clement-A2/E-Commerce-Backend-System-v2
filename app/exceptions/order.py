class OrderNotFoundError(Exception):
    pass

class OrderAlreadyExistsError(Exception):
    pass

class IncompleteOrderError(Exception):
    pass