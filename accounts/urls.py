from django.urls import path

from . import views


urlpatterns = [
    path('logout/', views.LogoutView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('register/', views.UserCreate.as_view()),
    path('all/', views.AccountsView.as_view()),
    path('vet/', views.VeterinaryView.as_view()),
    ]
