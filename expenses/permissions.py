from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

# class IsOwner2(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user\





class Roler1_5(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_roler1:
            return True
            # return bool(request.user and request.user.roler)
        if request.user.is_roler5:
            return True
            # return bool(request.user and request.user.roler)

    def has_object_permission(self, request, view, obj):
        if request.user.is_roler1 and request.method == "PUT":
            return True
        if request.user.is_roler1 and request.method == "DELETE":
            return True

        if request.user.is_roler1 and request.method == "POST":
            return True
        if request.user.is_roler1 and request.method == "GET":
            return True



class Roler2(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if request.user.roler=='roler2':
            return bool(request.user and request.user.roler)


class Roler3(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if request.user.roler=='roler3':
            return bool(request.user and request.user.roler)


class Roler4(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if request.user.roler=='roler4':
            return bool(request.user and request.user.roler)


class Roler5(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if request.user.roler=='roler5':
            return bool(request.user and request.user.roler)
