from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def example1(request):
    return HttpResponse("Hello world!")

def example2(request):
    return HttpResponse("Hello world, again!")
