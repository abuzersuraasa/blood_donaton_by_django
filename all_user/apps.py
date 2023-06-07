from django.apps import AppConfig


class AllUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'all_user'


class CustomerProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer_profile'


class HospitalProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hospital_profile'
