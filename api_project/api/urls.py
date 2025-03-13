# api_project/urls.py
from django.contrib import admin
from django.urls import path, include

from .views import BookList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the API app's URLs
    path('books/', BookList.as_view(), name='book-list'),  # Add the BookList view
]
