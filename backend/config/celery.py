import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('seatsprint')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery.schedules import crontab
app.conf.beat_schedule = {
    'expire-stale-holds': {
        'task': 'apps.bookings.tasks.expire_stale_holds',
        'schedule': 30.0,
    },
    'promote-waitlist': {
        'task': 'apps.waitlist.tasks.process_waitlist_promotions',
        'schedule': 60.0,
    },
    'expire-stale-waitlist-offers': {
        'task': 'apps.waitlist.tasks.expire_stale_offers',
        'schedule': 60.0,
    },
}
