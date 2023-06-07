from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """ User-Profile Serializer """
    class Meta:
        model = User
        # fields = ('name', 'email', 'user_type', 'password', 'mobile', 'user_id')
        fields = '__all__'

    def validate(self, data):
        for fields in data:
            if fields == "":
                raise serializers.ValidationError({'error': "empty field is not accepted "})
        return data


class CustomerProfileSerializer(serializers.ModelSerializer):
    """ Customer-Profile Serializer """
    class Meta:
        model = CustomerProfile
        fields = '__all__'

    def validate(self, data):

        for fields in data:
            if fields == "":
                raise serializers.ValidationError()

            return data


class HospitalProfileSerializer(serializers.ModelSerializer):
    """ Hospital-Profile Serializer """
    class Meta:
        model = HospitalProfile
        fields = '__all__'

    def validate(self, data):

        for fields in data:
            if fields == "":
                raise serializers.ValidationError()
            return data
