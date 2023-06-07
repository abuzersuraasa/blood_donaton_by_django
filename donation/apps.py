from django.apps import AppConfig


class RequestFulfilmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'request_fulfilment'


class UserBloodRequestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_blood_request'

    # def ready(self):
    #     pass
