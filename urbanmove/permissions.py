from rest_framework import permissions


class IsPassager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "passager"


class IsOperator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "operator"


class IsPassagerOrOperator(permissions.BasePermission):
    def has_permission(self, request, view):
        return IsPassager().has_permission(request, view) or IsOperator().has_permission(request, view)
