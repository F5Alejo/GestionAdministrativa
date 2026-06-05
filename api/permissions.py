from rest_framework.permissions import BasePermission


class EsAdministrador(BasePermission):
   from rest_framework.permissions import BasePermission


class EsAdministrador(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'destroy':
            return request.user and request.user.is_authenticated and request.user.is_staff
        return request.user and request.user.is_authenticated
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if view.action in ("list", "retrieve"):
            return True

        return user.is_staff
