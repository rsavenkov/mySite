from django.urls import path

from . import views

urlpatterns = [
    path('firstpage', views.firstpage),
    path('secondpage', views.secondpage),
    path('thirdpage', views.thirdpage),
]