from collections import defaultdict
from threading import local

class DomainEvent:
    pass

class EventDispatcher:
    _handlers = defaultdict(list)
    _thread_local = local()

    @classmethod
    def subscribe(cls, event_type, handler):
        cls._handlers[event_type].append(handler)

    @classmethod
    def dispatch(cls, event):
        if not hasattr(cls._thread_local, 'queue'):
            cls._thread_local.queue = []
        cls._thread_local.queue.append(event)

    @classmethod
    def flush(cls):
        if hasattr(cls._thread_local, 'queue'):
            events = cls._thread_local.queue
            cls._thread_local.queue = []
            for event in events:
                for handler in cls._handlers.get(type(event), []):
                    handler(event)
