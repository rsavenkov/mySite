from django.urls import path

from . import views

urlpatterns = [
    path('a', views.a, name = 'index'),
    path('b', views.b, name = 'index'),
    path('c', views.c),
]