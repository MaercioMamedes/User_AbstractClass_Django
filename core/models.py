from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    rg = models.CharField('RG', max_length=11)
    cpf = models.CharField('CPF', max_length=11)

    class Meta:
        abstract = True


class MyUser(CustomUser):
    pass
