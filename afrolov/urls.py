from django.urls import path

from afrolov import views

urlpatterns = [
    path('', views.index),
]

