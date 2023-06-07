from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *


""" Urls for Hospital/Blood-bank Inventory Detail's """
urlpatterns = [
    path('inventory/', InventoryGenerics.as_view()),
    path('inventory-up/<pk>/', InventoryupdateGenerics.as_view())
]
