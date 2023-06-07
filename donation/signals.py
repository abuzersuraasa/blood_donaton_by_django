# from django.db.models.signals import post_save
# from .models import *
# from django.dispatch import receiver
#
# def update_post(sender, instance, **kwargs):
#     print("inventory products updated")
#
#
# post_save.connect(update_post, sender=UserBloodRequestModel)
#
# @receiver(post_save, sender= UserBloodRequestModel)
# def inven(sender, instance, created, **kwargs):
#     if not created:
#