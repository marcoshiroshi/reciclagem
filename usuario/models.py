from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=300, blank=True)
    last_name = models.CharField(max_length=300, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


# class Morador(models.Model):
#
#     user = models.ForeignKey(User, models.DO_NOTHING, related_name='morador_user')
#     telefone = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
