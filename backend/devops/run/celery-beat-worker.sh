#!/usr/bin/env bash
# Note: The only work of this task is to send the periodic tasks to rabbit mq. See settings.CELERY_BEAT_SCHEDULE
# the worker defined in worker.sh will pick up and actually execute the tasks
celery -A configuration beat --loglevel=INFO
