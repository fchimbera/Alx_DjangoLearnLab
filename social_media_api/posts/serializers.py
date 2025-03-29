from rest_framework import serializers
from .models import Post, Comment

# PostSerializer is a serializer for the Post model. It converts model instances into JSON format and vice versa.
# It includes fields for the post's ID, author, title, content, and timestamps for creation and updates.
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']

# CommentSerializer is a serializer for the Comment model. It converts model instances into JSON format and vice versa.
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
