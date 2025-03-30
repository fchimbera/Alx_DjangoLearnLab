from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.viewsets import ViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from notifications.models import Notification
from .models import Post, Like
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED



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
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        pk = post_id
        post = generics.get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                content_type=ContentType.objects.get_for_model(post),
                object_id=post.id
            )
            return JsonResponse({'message': 'Post liked'}, status=201)
        return JsonResponse({'message': 'You already liked this post'}, status=200)


class UnLikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        pk = post_id
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(post=post, user=request.user).first()

        if like:
            like.delete()
            return JsonResponse({'message': 'Post unliked'}, status=200)

        return JsonResponse({'message': 'You have not liked this post yet'}, status=400)
