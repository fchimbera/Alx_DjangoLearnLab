from functools import wraps
from django.contrib.auth.decorators import permission_required

# Function that returns a function that checks if the user has the required role
def role_check(role):
    def has_role(user):
        return user.is_authenticated and user.userprofile.role == role
    return has_role

# Decorator that checks if the user has the required permission
def permission_required_decorator(permission):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            return permission_required(permission)(view_func)(request, *args, **kwargs)
        return _wrapped_view
    return decorator
