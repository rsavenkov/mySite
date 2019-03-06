from django.http import HttpResponse

def first(request):
    return HttpResponse("first")

def second(request):
    return HttpResponse("second")

def third(request):
    return HttpResponse("third")
