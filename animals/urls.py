from django.urls import path, re_path

from . import views

urlpatterns =[
    path('', views.AnimalView.as_view()),
    re_path('^(?P<pk>\d+)/$', views.DoctorAnimalDetailView.as_view()),
    path('my/', views.OwnerAnimalListView.as_view()),
    re_path('^my/(?P<pk>\d+)/$', views.OwnerAnimalDetailView.as_view())
]