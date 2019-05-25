from rest_framework import serializers
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer

from .models import MyUser, VeterinaryDoctor

from animals.serializers import AnimalSerializer


class UserSerializer(serializers.ModelSerializer):
    """
               This serializer inherits the Django serializers.
               It serializes the data for the creation of a new user.
               Fields included: id, user, name, surname, password, city, email, phone
               Write only fields: password
               Read only fields: id
               This Serializer overrides the create function

               """
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'name', 'surname', 'password', 'city', 'email', 'phone')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        """
                       Basic create function for the creation of new user.
                       it takes validated_data to make sure no errors occur upont registration.
                       password is not saved in plain text
                        but rather hashed before.
                       """
        username = MyUser.objects.create(
            username=validated_data['username'],
            name=validated_data['name'],
            surname=validated_data['surname'],
            city=validated_data['city'],
            email=validated_data['email']
        )

        username.set_password(validated_data['password'])
        username.save()
        return username


class VeterinaryDoctorsSerializer(serializers.ModelSerializer):
    """
                      This serializer inherits the Django serializers.
                      It serializes the data for listing all Veterinary Doctors.
                      Fields included: all for the specific model.

                      """

    class Meta:
        model = VeterinaryDoctor
        fields = ('__all__')


class AccountsSerializer(serializers.ModelSerializer):
    """
                  This serializer inherits the Django serializers.
                  It serializes the data for listing all registered users.
                  Fields included: id, user, name, surname, city, email, phone, animals
                  This serializer has a nested serializer 'AnimalSerializer, coming from
                  the animals application.

                  """
    animals = AnimalSerializer(many=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'name', 'surname', 'city', 'email', 'phone', 'animals')


class LoginSerializer(RestAuthLoginSerializer):
    """
                      This serializer inherits the Django Login Serializer.
                      The main purpose of this serializer is to remove the email field
                      from the login page, as it is not needed for the logic of this project.

                      """
    email = None
