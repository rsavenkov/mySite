from django.urls import path

from afrolov import views

urlpatterns = [
    path('', views.index),
    path('1', views.index1),
    path('2', views.submit, name = 'vote'),
    path('2', views.submit, name = 'vote'),
]

