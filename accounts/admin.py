from django.contrib import admin

from .models import *

admin.site.register(MyUser)
admin.site.register(VeterinaryDoctor)
admin.site.register(PetOwner)