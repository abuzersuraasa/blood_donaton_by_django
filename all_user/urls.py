from django.contrib import admin
from django.urls import path, include
from .views import *

""" Urls for All user including customer and hospital-profile's"""
urlpatterns = [

    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    path('all-user/', UserGenerics.as_view()),
    path('all-user/<id>/', UserupdateGenerics.as_view()),

    path('accounts/customer-profile/', CustomerGenerics.as_view()),
    path('accounts/customer-profile/<id>/', CustomerupdateGenerics.as_view()),

    path('accounts/hospital-details/', HospitalGenerics.as_view()),
    path('accounts/hospital-details/<id>/', HospitalupdateGenerics.as_view()),

]
