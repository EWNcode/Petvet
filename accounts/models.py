from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MinValueValidator
from django.db import models

from .enums import CityEnum, TitleEnum, DoctorTitle
from .validators import PhoneValidator

from common.validators import name_regex


class MyUser(AbstractUser):
    """
       An extension of the Django Abstract User.
       New fields: city, telephone.
       New regex for Name, Surname and phone.

       """
    phone_validator = PhoneValidator()

    name = models.CharField(validators=[name_regex], max_length=15, null=True, blank=True)
    surname = models.CharField(validators=[name_regex], max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, choices=[(c.name, c.value) for c in CityEnum])
    phone = models.CharField(validators=[phone_validator], max_length=10)


class VeterinaryDoctor(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=10, choices=[(t.name, t.value) for t in DoctorTitle])
    age = models.PositiveIntegerField(validators=[MinValueValidator(30)])

    def __str__(self):
        return f'{self.title} {self.user}'


class PetOwner(models.Model):
    username = models.OneToOneField(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'
