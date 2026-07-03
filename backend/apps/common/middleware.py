import uuid
import structlog
from threading import local

_thread_locals = local()

class RequestCorrelationIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        correlation_id = request.META.get('HTTP_X_CORRELATION_ID', str(uuid.uuid4()))
        _thread_locals.correlation_id = correlation_id
        structlog.contextvars.bind_contextvars(correlation_id=correlation_id)
        response = self.get_response(request)
        response['X-Correlation-ID'] = correlation_id
        structlog.contextvars.unbind_contextvars('correlation_id')
        return response

def get_correlation_id():
    return getattr(_thread_locals, 'correlation_id', None)
