from rest_framework.permissions import BasePermission

class IsAdminGroup(BasePermission):
    """Allows access only to members of the 'Admin' group."""
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Admin').exists()

class IsAdminOrFacultyGroup(BasePermission):
    """Allows access to members of the 'Admin' or 'Faculty' groups."""
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name__in=['Admin', 'Faculty']).exists()