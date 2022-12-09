import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

celery_app = Celery("braniac")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()


@celery_app.task
def add(x, y):
    z = x + y
    print(z)
