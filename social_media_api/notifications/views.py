from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def get_notifications(request):
    notifications = request.user.notifications.filter(read=False)
    data = [
        {
            'actor': notification.actor.username,
            'verb': notification.verb,
            'timestamp': notification.timestamp,
            'read': notification.read
        }
        for notification in notifications
    ]
    return JsonResponse({'notifications': data}, safe=False)

@login_required
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    notification.read = True
    notification.save()
    return JsonResponse({'message': 'Notification marked as read'}, status=200)
