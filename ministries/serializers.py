from rest_framework import serializers
from .models import Ministries

class MinistriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministries
        fields = ('__all__')