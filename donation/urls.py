from django.urls import path, include
from .views import *

""" Urls for Blood request fulfilment and Blood request Detail's """
urlpatterns = [
    path('fulfilment/', FulfilmentRequestGenerics.as_view()),
    path('fulfilment/<id>/', FulfilmentupdateGenerics.as_view()),
    path('bldrqs-dtls/', UserBloodRequestGenerics.as_view()),
    path('bldrqs-dtls/<id>/', UserBloodRequestupdateGenerics.as_view())
]
