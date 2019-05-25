from rest_framework.permissions import BasePermission


class CreateUserPermission(BasePermission):
    """
           This permission inherits the Django Base Permission.
           It allows only not Logged users,
           super or staff users to register new user.

           """

    def has_permission(self, request, view):
        """
                     This function is an override of the
                     has_permission function so that
                     it provides access only to non logged users,
                     or only to superusers and staff.

                     """
        if not request.user.is_authenticated or request.user.is_superuser or request.user.is_staff:
            return True


class LoggedPermission(BasePermission):
    """
        This permission inherits the Django Base Permission.
        It allows only logged users
        to see fields on the landed page.

           """

    def has_permission(self, request, view):
        """
                             This function is an override of the
                             has_permission function so that
                             it provides access only to logged users.

                             """

        if request.user and request.user.is_authenticated:
            return True
