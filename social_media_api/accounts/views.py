from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, generics
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions


class RegisterView(generics.GenericAPIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    permission_classes = [permissions.IsAuthenticated]
    # Check if the user is already followed
    user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)
    if user_to_follow != request.user:
        request.user.following.add(user_to_follow)
        return Response({'message': 'You are now following {}'.format(user_to_follow.username)})
    return Response({'message': 'You cannot follow yourself.'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    permission_classes = [permissions.IsAuthenticated]
    user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)
    if user_to_unfollow in request.user.following.all():
        request.user.following.remove(user_to_unfollow)
        return Response({'message': 'You have unfollowed {}'.format(user_to_unfollow.username)})
    return Response({'message': 'You are not following this user.'}, status=400)
