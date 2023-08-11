from django.contrib.auth.models import AbstractUser

from utilities.db import CommonInfo


# Create your models here.
class User(CommonInfo, AbstractUser):
    pass
