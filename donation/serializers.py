from rest_framework import serializers
from .models import *


class FulfilmentSerializer(serializers.ModelSerializer):
    """ Blood request Fulfilment Serializer """
    class Meta:
        model = Fulfilment
        fields = '__all__'

    def validate(self, data):

        for fields in data:
            if fields == "":
                raise serializers.ValidationError()
# {'error': "empty field is not accepted " }
            return data


class UserBloodRequestSerializer(serializers.ModelSerializer):
    """ Blood request Serializer for user """
    class Meta:
        model = UserBloodRequest
        fields = '__all__'

    def validate(self, data):

        for fields in data:
            if fields == "":
                raise serializers.ValidationError()
# {'error': "empty field is not accepted " }
            return data
