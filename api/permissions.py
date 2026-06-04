from rest_framework.permissions import BasePermission


class EsAdministrador(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'destroy':
            return request.user and request.user.is_authenticated and request.user.is_staff
        return request.user and request.user.is_authenticated
