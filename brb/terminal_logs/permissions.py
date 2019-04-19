from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Allow only owners to read/edit logs"""

    def has_object_permission(self, request, view, obj):
        print(request.user)
        return obj.user == request.user
