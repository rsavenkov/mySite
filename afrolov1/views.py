from django.http import HttpResponse


def abc(request):
    return HttpResponse("My test page!")