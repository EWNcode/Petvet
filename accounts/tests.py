from django.test import TestCase

from .models import MyUser, VeterinaryDoctor


class TestUserCreation(TestCase):
    """
    Test for auto user creation.
    """
    def test_profile(self):
      MyUser.objects.create_user(username="aloalo", password="password", email="abc@testmail.com", name='Ivan', surname='Ivanov', city='Sofia')


class TestDoctorCreation(TestCase):
    """
    Test for auto Veterinary Doctor creation.
    """
    def set_up_data(self):
        user = MyUser.objects.create_user(username="aloalo", password="password", email="abc@testmail.com", name='Ivan',
                                          surname='Ivanov', city='Sofia')

        VeterinaryDoctor.objects.create_user(user=user, title="Doctor", age="50")
