from rest_framework import serializers
from .models import *


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

    def validate(self, data):

        for fields in data:
            if fields == "":
                raise serializers.ValidationError()
            return data

