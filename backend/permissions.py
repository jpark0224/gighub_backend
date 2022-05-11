from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsArtist(permissions.BasePermission):
    message = 'You have to be a registered artist for this action.'

    def has_object_permission(self, request, view, obj):
        return request.user.is_artist
