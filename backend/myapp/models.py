from django.db import models

from utilities.db import CommonInfo


class MyApp(CommonInfo):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = "My App"
        verbose_name_plural = "My App"
