from django.urls import path

from . import views

urlpatterns = [
    path('fp', views.first, name="first"),
    path('sp', views.second, name="second"),
    path('tp', views.third, name="third"),
]