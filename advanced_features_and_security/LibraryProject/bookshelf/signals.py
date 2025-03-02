from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Article

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == "book":
        content_type = ContentType.objects.get_for_model(Article)

        # Define permissions
        permissions = {
            "can_view": "Can view books",
            "can_create": "Can create books",
            "can_edit": "Can edit books",
            "can_delete": "Can delete books",
        }

        # Create or update groups
        group_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_edit", "can_create"],
            "Admins": ["can_view", "can_edit", "can_create", "can_delete"],
        }

        for perm_codename, perm_name in permissions.items():
            Permission.objects.get_or_create(codename=perm_codename, name=perm_name, content_type=content_type)

        for group_name, perm_codenames in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_codename in perm_codenames:
                permission = Permission.objects.get(codename=perm_codename)
                group.permissions.add(permission)