from django.urls import path

from . import views

urlpatterns = [
    path('example1', views.example1),
    path('example2', views.example2),
]