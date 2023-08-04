import os

from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand
from structlog import getLogger

from django.contrib.auth import get_user_model
User = get_user_model()

logger = getLogger(__file__)


class Command(BaseCommand):
    """
    Create the superuser
    """

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(
            email=os.environ.get("SUPER_USER_EMAIL"),
            defaults=dict(
                username=os.environ.get("SUPER_USERNAME"),
                is_staff=True,
                is_superuser=True,
                password=make_password(os.environ.get("SUPER_PASSWORD")),
                is_active=True,
            ),
        )

        logger.info(f"{user.email} has been {'created' if created else 'found'}")
