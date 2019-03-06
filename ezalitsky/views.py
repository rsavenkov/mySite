#import moduls
from django.shortcuts import render
from django.http import HttpResponse

# Create views.
def firstpage(request):
    return HttpResponse("polls index firstpage")

def secondpage(request):
    return HttpResponse("polls index secondpage")

def thirdpage(request):
    return HttpResponse("polls index thirdpage")