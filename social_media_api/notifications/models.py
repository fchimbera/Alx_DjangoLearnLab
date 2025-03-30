from django.db import models
from django.conf import settings
from accounts.models import CustomUser
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Notification model representing a notification in the application.
# Each notification has a recipient (linked to the User model), a message, a timestamp, and a read status.
class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='actor_notifications', null=True, blank=True)
    verb = models.CharField(max_length=255, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Notification for {self.recipient.username}: {self.message}'
