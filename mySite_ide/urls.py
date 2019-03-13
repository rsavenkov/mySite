"""mySite_ide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('aklimenko/', include('aklimenko.urls')),
    path('afrolov/', include('afrolov.urls')),
    path('dtemen/', include('dtemen.urls')),
    path('rklimenko/', include('rklimenko.urls')),
    path('rsavenkov/', include('rsavenkov.urls')),
    path('admin/', admin.site.urls),
    url(r'^vinog/', include('pvinogradov.urls')),
    path('polls/', include('polls.urls')),
    path('mshirinskiy/', include('mshirinskiy.urls')),
    path('ezalitsky/', include('ezalitsky.urls')),
    path('Ematsyuk/', include('Ematsyuk.urls')),
    path('aleviev/', include('aleviev.urls')),
    path('kdrozdov/', include('kdrozdov.urls')),
]
