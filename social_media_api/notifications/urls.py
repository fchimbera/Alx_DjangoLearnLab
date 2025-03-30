from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_notifications, name='notifications'),
    path('<int:notification_id>/mark-as-read/', views.mark_as_read, name='mark-as-read'),
]
