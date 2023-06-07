from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *


class UserModel(AbstractUser):
    """ User-Model """
    username = None
    first_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=50)
    user_type = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class CustomerProfile(models.Model):
    """ Customer-Profile Model """
    user = models.ForeignKey(UserModel, models.DO_NOTHING, blank=True, null=True)
    age = models.CharField(max_length=3)
    sex = models.CharField(max_length=1)
    blood_group = models.CharField(max_length=3)
    address = models.CharField(max_length=300)


class HospitalProfile(models.Model):
    """ Hospital-Profile Model """
    user = models.ForeignKey(UserModel, models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
