import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    event_type = django_filters.ChoiceFilter(choices=Event.EventType.choices)
    is_active = django_filters.BooleanFilter()
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Event
        fields = ['event_type', 'is_active', 'title']
