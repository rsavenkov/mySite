from django.urls import path
from . import views

urlpatterns = [
    path('rklim', views.rklim)
]