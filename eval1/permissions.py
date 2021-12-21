from rest_framework import permissions

class ConsumerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class ProducrPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff
