from rest_framework import generics, status
from rest_framework.response import Response
from rest_auth.views import LoginView as RestLoginView, LogoutView as RestLogoutView, PasswordResetView as RestAuthPasswordResetView, PasswordChangeView as RestAuthPasswordChangeView
from rest_framework.permissions import AllowAny



from .permissions import LoggedPermission, CreateUserPermission, LoginPermission
from .serializers import UserSerializer, AccountsSerializer, VeterinaryDoctorsSerializer, LoginSerializer
from .models import MyUser, VeterinaryDoctor


class UserCreate(generics.CreateAPIView):
    """
                          This view inherits the Django generic views.
                          It represents how the register form looks on
                          the website.
                          Serializer used: UserSerializer
                          """
    serializer_class = UserSerializer

    def post(self, request):
        """
                the override of the post function
                with a response 'Success' if the saved serialized
                data provided by the person meets the database requirements
                """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response('SUCCESS', status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    permission_classes = (CreateUserPermission,)


class AccountsView(generics.ListAPIView):
    """
                              This view inherits the Django generic views.
                              This view renders how the list of accounts that are shown
                              on the website.
                              Serializer used: AccountsSerializer
                              """
    def get_queryset(self):
        """
                        the override of the get_queryset function.
                        this function give the user ability to filter
                        the accounts by their ID, and filter the
                        queryset by that id. If ID is not provided
                        the queryset stays the same and shows all accounts.
                        """
        id = self.request.query_params.get('id', None)

        if id is not None:
            queryset = MyUser.objects.filter(id=id)
        else:
            queryset = MyUser.objects.all()
        return queryset

    serializer_class = AccountsSerializer
    permission_classes = (AllowAny,)


class VeterinaryView(generics.ListAPIView):
    """
                              This view inherits the Django generic views.
                              This view renders how the list of accounts that are
                                reigstered as Veterinary doctors and are shown
                              on the website.
                              Serializer used: VeterinaryDoctorsSerializer
                              """
    def get_queryset(self):
        """
                                the override of the get_queryset function.
                                this function give the user ability to filter
                                the Veterinary doctors by their ID, and filter the
                                queryset by that id. If ID is not provided
                                the queryset stays the same and shows all accounts.
                                """
        id = self.request.query_params.get('id', None)

        if id is not None:
            queryset = VeterinaryDoctor.objects.filter(id=id)
        else:
            queryset = VeterinaryDoctor.objects.all()
        return queryset

    serializer_class = VeterinaryDoctorsSerializer
    permission_classes = (AllowAny,)


class LoginView(RestLoginView):
    """
                                 This view inherits the Django LoginView.
                                 This view renders how the fields required for the login
                                 are shown on the page.
                                 Serializer used: LoginSerializer
                                 """
    queryset = MyUser.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (LoginPermission,)


class LogoutView(RestLogoutView):
    """
                                     This view inherits the Django LoginView.
                                     This view renders how the fields required for the logout
                                     are shown on the page.
                                     Serializer used: LoginSerializer
                                     """

    permission_classes = (LoggedPermission,)


class PasswordChangeView(RestAuthPasswordChangeView):
    """
    This view inherits the Django PasswordChangeView.
    """

    permission_classes = (LoggedPermission,)


class PasswordResetView(RestAuthPasswordResetView):
    """
       This view inherits the Django PasswordResetView.
       """

    permission_classes = (AllowAny,)