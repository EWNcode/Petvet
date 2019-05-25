from rest_framework.permissions import SAFE_METHODS, BasePermission


from accounts.models import VeterinaryDoctor


class AnimalCreatePermission(BasePermission):
    """
               This permission inherits the Django Base Permission.
               It allows only not Logged users,
               super or staff users to register new user.
               This permission restricts Veterinary doctors from
               creating an Animal

               """

    def has_permission(self, request, view):
        """
                             This function is an override of the
                             Django Base permission function so that
                             it provides access only to logged users,
                             which are not doctors, to create an animal.
                             Super and staff users have the same authorization.

                             """
        user = VeterinaryDoctor.objects.filter(user=request.user).exists()

        if request.method == 'GET':
            return True

        if request.user.is_staff or not user or (request.user.is_superuser and not request.method == 'POST'):
            return True
        return False


class IsDoctor(BasePermission):
    """
                   This permission inherits the Django Base Permission.
                   It allows only Veterinary Doctors, super and staff users
                    to edit specific fields, from the model.animal.

                   """

    def has_object_permission(self, request, view, obj):
        """
                                     This function is an override of the
                                     Django Base permission function so that
                                     it provides access only to logged users,
                                     which are doctors, to edit an animal.
                                     Super and staff users have the same authorization.

                                     """

        if VeterinaryDoctor.objects.filter(user=request.user).exists() or request.user.is_superuser or request.user.is_staff:
            return True


class IsOwner(BasePermission):
    """
                      This permission inherits the Django Base Permission.
                      It allows only Owners to see their own pets, also super
                      and staff users. It allows those users to edit specific fields,
                      from the model.animal. This permission restricts Veterinary doctors from
                      creating an Animal

                      """

    def has_object_permission(self, request, view, obj):
        """
                              This function is an override of the
                                Django Base permission function so that
                                it provides access only to logged users,
                                which are owners of a specific pet, to edit specific fields.
                                Super and staff users have the same authorization.

                              """

        return obj.owner == request.user or request.user.is_superuser or request.user.is_staff
