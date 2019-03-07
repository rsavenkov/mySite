from django.urls import path

from django.conf.urls import url

from pvinogradov import views

urlpatterns = [
    # url(r'^page1/', views.fn),
    path('test', views.test),
    path('test1', views.test),
    path('test2', views.test)

]
