from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user

class IsRequestingUserOrReadOnly(permissions.BasePermission):
    message = 'You have to log in as this user for this action.'

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.username == request.user.username

class IsGroupEditor(permissions.BasePermission):
    message = 'You have to be a group editor for this action.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.groups.filter(name='Group Editors').exists()


class IsArtist(permissions.BasePermission):
    message = 'You have to be a registered artist for this action.'

    def has_object_permission(self, request, view, obj):
        return request.user.is_artist
