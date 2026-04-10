from rest_framework import permissions


class IsVendorUser(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'vendor' role to
    create or edit resources.
    """

    def has_permission(self, request, view):
        # Allow read-only actions (GET, HEAD, OPTIONS) for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is logged in and has the vendor role
        return (
            request.user.is_authenticated
            and hasattr(request.user, "profile")
            and request.user.profile.role == "vendor"
        )


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the store owner is the requesting user
        # (For products, it checks obj.store.vendor)
        if hasattr(obj, "vendor"):
            return obj.vendor == request.user
        if hasattr(obj, "store"):
            return obj.store.vendor == request.user
        return False
