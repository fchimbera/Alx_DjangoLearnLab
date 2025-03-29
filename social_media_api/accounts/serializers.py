from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        token, created = Token.objects.get_or_create(user=user)
        return {'user': user, 'token': token.key}
        return user
        raise serializers.ValidationError("Invalid credentials")
