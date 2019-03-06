from django.urls import path

from . import views

urlpatterns = [
    path('fp', views.fp, name="first"),
    path('sp', views.sp, name="second"),
    path('tp', views.tp, name="third"),
]