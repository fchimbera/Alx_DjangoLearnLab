from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
<<<<<<< HEAD
from rest_framework.authtoken.models import Token
=======
>>>>>>> ba2a36e75e3fe3278aa47f6e002bb2635cec0d02

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
<<<<<<< HEAD
        token, created = Token.objects.get_or_create(user=user)
        return {'user': user, 'token': token.key}
        return user
=======
        if user and user.is_active:
            return user
>>>>>>> ba2a36e75e3fe3278aa47f6e002bb2635cec0d02
        raise serializers.ValidationError("Invalid credentials")
