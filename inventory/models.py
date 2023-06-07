from django.db import models

from all_user.models import UserModel


class Inventory(models.Model):
    """ Inventory Model for Hospital and Blood-Bank """
    user = models.ForeignKey(UserModel, models.DO_NOTHING, blank=True, null=True)
    user_type = models.CharField(max_length=10, blank=True, null=True)
    blood_group_type = models.CharField(max_length=3, blank=True, null=True)
    quantity_available = models.CharField(max_length=3, blank=True, null=True)
