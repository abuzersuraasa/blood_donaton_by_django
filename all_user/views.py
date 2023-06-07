from .serializers import *
from django.contrib import admin
from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib.auth import get_user_model
admin.autodiscover()
User = get_user_model()


class UserGenerics(generics.ListCreateAPIView):
    """Views for creating and Retrieving list of all User """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


# class UserList(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetails(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserupdateGenerics(generics.RetrieveUpdateDestroyAPIView):
    """Views for Updating, Deleting and Retrieving list of any specific Users """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class CustomerGenerics(generics.ListCreateAPIView, generics.CreateAPIView):
    """Views for creating Customer-Profiles """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer


class CustomerupdateGenerics(generics.RetrieveUpdateDestroyAPIView):
    """Views for Updating, Deleting and Retrieving list of all Customer Profiles """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    lookup_field = 'id'


class HospitalGenerics(generics.ListCreateAPIView, generics.CreateAPIView):
    """Views for creating Hospital-Profiles """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = HospitalProfile.objects.all()
    serializer_class = HospitalProfileSerializer


class HospitalupdateGenerics(generics.RetrieveUpdateDestroyAPIView):
    """Views for Updating, Deleting and Retrieving list of all Hospital Profiles """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = HospitalProfile.objects.all()
    serializer_class = HospitalProfileSerializer
    lookup_field = 'id'


