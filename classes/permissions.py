from rest_framework import permissions
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Read-only permissions are allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the Teacher of the class
        return obj.teacher == request.user