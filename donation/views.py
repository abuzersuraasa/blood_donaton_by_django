from .serializers import *
from rest_framework import generics
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions


class FulfilmentRequestGenerics(generics.ListCreateAPIView, generics.CreateAPIView):
    """Views for creating Fulfilment """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Fulfilment.objects.all()
    serializer_class = FulfilmentSerializer


class FulfilmentupdateGenerics(generics.RetrieveUpdateDestroyAPIView):
    """Views for Updating Request Fulfilment """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Fulfilment.objects.all()
    serializer_class = FulfilmentSerializer
    lookup_field = 'id'


class UserBloodRequestGenerics(generics.ListCreateAPIView, generics.CreateAPIView):
    """Views for creating User Blood Request """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = UserBloodRequest.objects.all()
    serializer_class = UserBloodRequestSerializer


class UserBloodRequestupdateGenerics(generics.RetrieveUpdateDestroyAPIView):
    """Views for updating User Blood Request """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = UserBloodRequest.objects.all()
    serializer_class = UserBloodRequestSerializer
    lookup_field = 'id'
