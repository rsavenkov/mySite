from django.urls import path

from . import views

urlpatterns = [
    path('kf', views.kf, name='kf'),
]