from django.test import TestCase

from .models import Animal

from accounts.models import MyUser


class AnimalCreation(TestCase):
    """
    Test for auto Animal creation
    """
    def set_up_data(self):
        user = MyUser.objects.create_user(username="aloalo", password="password", email="abc@testmail.com", name='Ivan',
                                          surname='Ivanov', city='Sofia')

        Animal.objects.create_user(name='Barri', gender='Male', kind='Dog', birthday='2014-08-05', serial_number='1020304050', general_information='магаре', owner=user)
