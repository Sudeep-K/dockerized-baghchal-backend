import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baghchal.settings")

app = Celery("baghchal", backend="redis://redis:6379/1", broker="redis://redis:6379/0")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "run-every-10-seconds": {
        "task": "baghchal.tasks.foo",
        "schedule": timedelta(seconds=10),
    },
    "run-every-1800-seconds": {
        "task": "baghchal.tasks.bar",
        "schedule": timedelta(seconds=1800),
    },
}
