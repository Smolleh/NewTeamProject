from rest_framework.permissions import BasePermission

class AlwaysAllowCurator(BasePermission):
    def has_permission(self, request, view):
        return True
    