from rest_framework import BasePermission

class AlwaysAllowCurator(BasePermission):
    def has_permission(self, request, view):
        return True
    