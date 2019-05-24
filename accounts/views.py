from rest_framework import generics, status
from rest_framework.response import Response

from .permissions import CreateUserPermission
from .serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response('SUCCESS', status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    permission_classes = (CreateUserPermission,)