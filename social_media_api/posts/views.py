from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.viewsets import ViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#@api_view(['GET'])
#@permission_classes([IsAuthenticated])
#def user_feed(request):
    # Get the users the current user is following
    #followed_users = request.user.following.all()
    
    # Fetch posts created by the followed users, ordered by creation date
    #posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    
    # Serialize the posts (ensure you have a PostSerializer)
    #from .serializers import PostSerializer
    #serializer = PostSerializer(posts, many=True)

    #return Response(serializer.data) 

class FeedViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # Get the posts from followed users
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)