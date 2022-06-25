from rest_framework.permissions import BasePermission



class IsPersonUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_client)


class IsCompanyUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_freecancer)