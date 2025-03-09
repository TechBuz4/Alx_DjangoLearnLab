from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission that grants read-only access to regular users
    and full access to admin users.
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:  # Allow read access to all
            return True
        return request.user and request.user.is_staff  # Only admins can modify
