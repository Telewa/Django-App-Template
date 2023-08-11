from __future__ import absolute_import

import os

from celery import Celery
from celery.signals import worker_process_shutdown, worker_process_init
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configuration.settings")

app = Celery("configuration")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@worker_process_init.connect
def init_worker(**kwargs):
    print("Worker initialized.")


@worker_process_shutdown.connect
def shutdown_worker(**kwargs):
    print("Worker shut down.")
