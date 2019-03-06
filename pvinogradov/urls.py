from django.conf.urls import url

from mySite_ide import views

urlpatterns = [
    url(r'^page1/', views.fn),

]
