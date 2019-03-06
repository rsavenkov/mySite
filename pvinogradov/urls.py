from django.conf.urls import url

from first.page import views

urlpatterns = [
    url(r'^page1/', views.fn),

]
