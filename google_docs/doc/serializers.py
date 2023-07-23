from rest_framework import serializers
from .models import Doc

class DocSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=True)
    content = serializers.CharField

    class Meta:
        model = Doc
        fields = '__all__'
