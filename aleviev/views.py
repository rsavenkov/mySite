from django.shortcuts import render
from django.http import HttpResponse

def planet(request):
    return HttpResponse("Earth")

def country(request):
    return HttpResponse("Russian Federation")

def city(request):
    return HttpResponse("Moscow")