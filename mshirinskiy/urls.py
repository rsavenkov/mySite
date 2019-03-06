from django.urls import path

from . import views

urlpatterns = [
    path('SW', views.obi, name='obi'),
    path('AC0', views.pixy, name='pixy'),
    path('AC6', views.talisman, name='talisman'),
    path('AC5', views.blaze, name='blaze'),
    path('AC3', views.dision, name='dision'),
]