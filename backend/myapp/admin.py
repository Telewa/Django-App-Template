from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ImportExportActionModelAdmin

from myapp.models import MyApp


@admin.register(MyApp)
class MyAppAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = (
        "id",
        "name",
    )
