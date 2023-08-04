from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from account.models import User


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return

        # Allow sign in with username or email
        user = (
            User.objects.filter(
                Q(username__iexact=username) | Q(email__iexact=username)
            )
            .order_by("id")
            .first()
        )

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
