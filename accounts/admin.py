from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class MyUserAdmin(UserAdmin):
    """
                 This class inherits the Django User admin
                 so that the admin panel knows how to handle
                 the hashing of user created trough the projects
                 admin panel.

                 """
    pass

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(VeterinaryDoctor)
