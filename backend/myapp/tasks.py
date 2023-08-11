from datetime import datetime

from celery import shared_task
from structlog import getLogger

from utilities.coding import KE_TIMEZONE

logger = getLogger(__name__)


@shared_task(bind=True, name="every_minute_task")
def every_minute_task(self, **kwargs):
    current_time = datetime.now(KE_TIMEZONE).isoformat()
    logger.info(f"The time now is: {current_time}")
