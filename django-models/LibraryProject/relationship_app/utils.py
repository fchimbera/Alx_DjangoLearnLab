def role_check(role):
    def has_role(user):
        return user.is_authenticated and user.userprofile.role == role
    return has_role