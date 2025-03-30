from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedViewSet, LikePostView, UnLikePostView
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'feed', FeedViewSet, basename='feed')

urlpatterns = router.urls
urlpatterns += [
 #   path('feed/', FeedViewSet.as_view(), name='feed'),
    path('<int:pk>/like/', LikePostView.as_view, name='like-post'),
    path('<int:pk>/unlike/', UnLikePostView.as_view, name='unlike-post'),
]