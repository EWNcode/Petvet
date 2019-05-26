from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('animal/', include('animals.urls')),
    path('register/', include('rest_auth.registration.urls')),

]
