from django.urls import path

from . import views

urlpatterns = [
    path('planet', views.planet, name='planet'),
    path('country', views.country, name='country'),
    path('city', views.planet, name='city'),
]