from django.urls import path

from . import views

app_name = 'afrolov1'
urlpatterns = [
    path('abc', views.abc),
]