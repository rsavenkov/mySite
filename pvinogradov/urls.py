from django.conf.urls import url

from pvinogradov import views

urlpatterns = [
    url(r'^page1/', views.fn),

]
