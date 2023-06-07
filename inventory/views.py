from .serializers import *
from rest_framework import generics
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions


class InventoryGenerics(generics.ListCreateAPIView, generics.CreateAPIView):
    """Views for Inventory """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryupdateGenerics(generics.RetrieveUpdateDestroyAPIView):
    """Views for updating Inventory """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    lookup_field = 'id'
