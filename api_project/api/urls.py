
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from .views import BookList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the API app's URLs
    path('books/', BookList.as_view(), name='book-list'),  # Add the BookList view
]

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]
