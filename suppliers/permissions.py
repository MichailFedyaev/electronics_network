from rest_framework import permissions


class IsActiveStaff(permissions.BasePermission):
    """Доступ только для активных сотрудников"""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active and request.user.is_staff)