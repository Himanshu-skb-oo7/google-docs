from rest_framework import serializers
from .models import Doc
from users.models import CustomUser


class EmailField(serializers.Field):
    def to_internal_value(self, data):
        try:
            print(data)
            user = CustomUser.objects.get(email=data)
            return user
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
    
    def to_representation(self, value):
        return [user.email for user in value.all()]

    
class DocListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc
        fields = ('id', 'title')  # Specify the limited fields for the list API


class DocDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc
        fields =('id', 'title', 'content')  # Include all fields for the details API


class DocUpdateSerializer(serializers.ModelSerializer):
    shared_with = EmailField(allow_null=True, required=False)
    title = serializers.CharField(required=False)

    class Meta:
        model = Doc
        fields = ('shared_with', 'title', 'content')

    def update(self, instance, validated_data):
        shared_with = validated_data.pop('shared_with', None)
        
        if shared_with is not None:
            instance.shared_with.add(shared_with)
        
        return super().update(instance, validated_data)


class DocCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = ['id', 'title', 'content']  # Include the relevant fields