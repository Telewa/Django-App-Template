from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin

from account.models import User


@admin.register(User)
class UserAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "last_name",
        "first_name",
        "is_superuser",
        "is_active",
    )
    list_filter = ("is_active",)
    ordering = ("id",)
