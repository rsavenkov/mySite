from django.http import HttpResponse


def a(request):
    return HttpResponse("a")

def b(request):
    return HttpResponse("b")

def c(request):
    return HttpResponse("c")