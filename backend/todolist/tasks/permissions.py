from rest_framework import permissions


class IsTaskOwnerOrReadOnly(permissions.BasePermission):
    message = "Вы не являетесь владельцем этой задачи"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
