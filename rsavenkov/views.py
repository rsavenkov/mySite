from django.http import HttpResponse


def test(request):
    return HttpResponse("My test page!")