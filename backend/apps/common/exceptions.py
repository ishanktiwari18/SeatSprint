class BusinessException(Exception):
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        super().__init__(message)

class SeatsUnavailableException(BusinessException):
    def __init__(self, message="Seats are not available."):
        super().__init__(message, code='seats_unavailable')

class InvalidStateTransition(BusinessException):
    def __init__(self, message="Invalid state transition."):
        super().__init__(message, code='invalid_state_transition')

class PaymentFailedException(BusinessException):
    def __init__(self, message="Payment failed."):
        super().__init__(message, code='payment_failed')

class ShowCancelledException(BusinessException):
    def __init__(self, message="Show is cancelled."):
        super().__init__(message, code='show_cancelled')
