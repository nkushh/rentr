from rest_framework import serializers
from . import models as auth_models
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth_models.User
        fields = ('id', 'username', 'email', 'password', 'user_type', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = auth_models.User.objects.create(
            username=validated_data['username'].lower(),
            email=validated_data['email'],
            user_type=validated_data.get('user_type', 2),
            phone_number=validated_data.get('phone_number', '')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)