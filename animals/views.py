from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Animal
from .serializers import AnimalSerializer, AnimalCreateSerializer, DoctorAnimalEditSerializer
from .permissions import AnimalCreatePermission, IsDoctor, IsOwner

from common.views import MethodSerializerView


class AnimalView(MethodSerializerView, generics.ListCreateAPIView):
    """
                                  This view inherits the Django generic views.
                                  This view renders how the list of animals that are
                                    registered as on the website are shown
                                  on the page.
                                  Serializer used: VeterinaryDoctorsSerializer
                                  If the method is GET: Serializer is : AnimalSerializer
                                  For the POST method the Serializer is: AnimalCreateSerializer
                                  """
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    method_serializer_classes = {
        ('GET'): AnimalSerializer,
        ('POST'): AnimalCreateSerializer,
    }

    permission_classes = (IsAuthenticated, AnimalCreatePermission)


class OwnerAnimalListView(generics.ListAPIView):
    """
                                      This view inherits the Django generic views.
                                      This view renders how the list of animals that are
                                        registered by the request.user as on the website are shown
                                      on the page.
                                      Serializer used: AnimalSerializer
                                      """

    def get_queryset(self):
        """
                                        the override of the get_queryset function.
                                        This function give the user/owner ability to filter
                                        the animals by their kind, and filter the
                                        queryset by that kind. If kind is not provided
                                        the queryset stays the same and shows all owners animals.
                                        """
        kind = self.request.query_params.get('k', None)

        if kind is not None:
            queryset = Animal.objects.filter(kind=kind)
        else:
            queryset = Animal.objects.all().filter(owner=self.request.user)
        return queryset

    serializer_class = AnimalSerializer

    permission_classes = (IsAuthenticated, IsOwner)


class OwnerAnimalDetailView(MethodSerializerView, generics.RetrieveUpdateDestroyAPIView):
    """
                                          This view inherits the Django generic views.
                                          This view renders how the filtered list of animals(by id) that are
                                            registered by the request.user as on the website are shown
                                          on the page.
                                          Serializer used: AnimalCreateSerializer
                                          """
    queryset = Animal.objects.all()

    method_serializer_classes = {
        ('GET'): AnimalSerializer,
        ('PUT', 'PATCH'): AnimalCreateSerializer,

    }

    permission_classes = (IsAuthenticated, AnimalCreatePermission, IsOwner)


class DoctorAnimalDetailView(MethodSerializerView, generics.RetrieveUpdateDestroyAPIView):
    """
                                              This view inherits the Django generic views.
                                              This view renders how the filtered list of animals(by id) that are
                                                registered by the request.user(not owner) as on the website are shown
                                              on the page.
                                              Serializer used: AnimalCreateSerializer
                                              """

    def get_queryset(self):
        """
                        the override of the get_queryset function.
                        This function give the user/doctor ability to filter
                        the animals by their kind, and filter the
                        queryset by that kind. If kind is not provided
                        the queryset stays the same and shows animals.
                        """
        kind = self.request.query_params.get('k', None)

        if kind is not None:
            queryset = Animal.objects.filter(kind=kind)
        else:
            queryset = Animal.objects.all()
        return queryset

    method_serializer_classes = {
        ('GET'): AnimalSerializer,
        ('PUT', 'PATCH'): DoctorAnimalEditSerializer,

    }

    permission_classes = (IsAuthenticated, IsDoctor)