from django.db import models

from .enums import AnimalKind, Gender
from .validators import SerialNumberValidator

from common.validators import NameValidator
from accounts.models import MyUser


class Animal(models.Model):
    """
               This model handles the fields required
               for the registration of an animal by logged user.
               Fields: user, gender, kind, birthday, serial number,
               general information and vaccines.
               Owner field of this model is a a foreignkey from accounts.Myuser


               """
    name_validator = NameValidator()
    serial_number = SerialNumberValidator()

    name = models.CharField(validators=[name_validator], max_length=10)
    gender = models.CharField(max_length=6, choices=[(gender.name, gender.value) for gender in Gender])
    kind = models.CharField(max_length=3, choices=[(kind.name, kind.value) for kind in AnimalKind])
    birthday = models.DateField()
    serial_number = models.CharField(validators=[serial_number], max_length=10, unique=True)
    general_information = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    vaccine_1 = models.BooleanField(null=True)
    vaccine_1_date = models.DateField(null=True)
    vaccine_2 = models.BooleanField(null=True)
    vaccine_2_date = models.DateField(null=True)
    vaccine_3 = models.BooleanField(null=True)
    vaccine_3_date = models.DateField(null=True)
    vaccine_4 = models.BooleanField(null=True)
    vaccine_4_date = models.DateField(null=True)

