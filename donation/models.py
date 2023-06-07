from django.db import models

from all_user.models import UserModel


class Fulfilment(models.Model):
    """ Blood request Fulfilment Model """
    user = models.ForeignKey(UserModel, models.DO_NOTHING, blank=True, null=True)
    blood_group_type = models.CharField(max_length=3, blank=True, null=True)
    quantity_fulfilled = models.CharField(max_length=3, blank=True, null=True)
    fulfilled_by = models.CharField(max_length=20, blank=True, null=True)


class UserBloodRequest(models.Model):
    """ Blood request Model for User """
    user = models.ForeignKey(UserModel, models.DO_NOTHING, blank=True, null=True)
    blood_group_type = models.CharField(max_length=3, blank=True, null=True)
    quantity_required = models.CharField(max_length=3, blank=True, null=True)
    quantity_fulfilled = models.CharField(max_length=3, blank=True, null=True)