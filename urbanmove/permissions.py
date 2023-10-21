from rest_framework import permissions


class IsOperator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "operator"
