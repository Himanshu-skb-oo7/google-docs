from rest_framework import serializers
from .models import Doc

class DocListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc
        fields = ('id', 'title')  # Specify the limited fields for the list API

class DocDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc
        fields = '__all__'  # Include all fields for the details API
