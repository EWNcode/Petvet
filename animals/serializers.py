from rest_framework import serializers
from rest_framework import exceptions

from .models import Animal


from accounts.models import MyUser

class AnimalSerializer(serializers.ModelSerializer):
    """
                          This serializer inherits the Django serializers.
                          It serializes the data for listing all Animals in the
                          database.
                          Fields included: all for the specific model.

                          """
    class Meta:
        model = Animal
        fields = ('__all__')


class AnimalCreateSerializer(serializers.ModelSerializer):
    """
            This serializer inherits the Django serializers.
            It serializes the data for listing all Animal fields
            that the owner/user(only not doctor) must add in order to register
            his/her pet
            Fields included: name, gender, kind, birthday

            """
    class Meta:
        model = Animal
        fields = ('name', 'gender', 'kind', 'birthday')

    def create(self, validated_data):
        owner = MyUser.objects.get(username=self.context['request'].user)
        validated_data['owner'] = owner
        return super(AnimalCreateSerializer, self).create(validated_data)


class DoctorAnimalEditSerializer(serializers.ModelSerializer):
    """
            This serializer inherits the Django serializers.
            It serializes the data for listing all Animal fields
            that the doctor/user(only not owner) must add in order
            to add fields only allowed by this types of users.
            Exclude included: name, gender, kind, birthday

            """

    class Meta:
        model = Animal
        exclude = ('name', 'gender', 'kind', 'birthday', 'owner')
#