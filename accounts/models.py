from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from .enums import CityEnum, DoctorTitle
from .validators import PhoneValidator

from common.validators import NameValidator


class MyUser(AbstractUser):
    """
       An extension of the Django Abstract User.
       New fields: city, telephone.
       New property: animals.
       New regex for Name, Surname and phone.
       All fields are required and cannot be null.

       """
    phone_validator = PhoneValidator()
    name_validator = NameValidator()

    name = models.CharField(validators=[name_validator], max_length=15, null=False, blank=False)
    surname = models.CharField(validators=[name_validator], max_length=20, null=False, blank=False)
    city = models.CharField(max_length=20, choices=[(c.name, c.value) for c in CityEnum], null=False, blank=False)
    phone = models.CharField(validators=[phone_validator], max_length=10)

    @property
    def animals(self):
        return self.animal_set.all()


class VeterinaryDoctor(models.Model):
    """
           Veterinary Doctor User.
           One to one field with MyUser.
           Fields: user, title, age

           """

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=10, choices=[(t.name, t.value) for t in DoctorTitle])
    age = models.PositiveIntegerField(validators=[MinValueValidator(30)])

    def __str__(self):
        return f'{self.title} {self.user}'
