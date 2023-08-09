from rest_framework.permissions import BasePermission

class IsOwnerOrShared(BasePermission):
    """
    Custom permission to allow access to owners or users shared with the document.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the document.
        if obj.owner == request.user:
            return True

        # Check if the user is in the shared_with list.
        print(obj.shared_with.all());
        return request.user in obj.shared_with.all()
