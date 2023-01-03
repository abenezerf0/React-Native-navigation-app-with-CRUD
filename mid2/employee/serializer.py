from rest_framework import serializers
from .models import employee

class empSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'