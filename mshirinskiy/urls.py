from django.urls import path

from . import views

urlpatterns = [
    path('msh', views.mshirinskiy, name='mshirinskiy'),
]