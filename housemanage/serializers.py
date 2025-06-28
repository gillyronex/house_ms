from .models import *
from rest_framework import serializers

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['name', 'email', 'phone']
