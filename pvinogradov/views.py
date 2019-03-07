from django.http import HttpResponse
# from django.shortcuts import render
# from .forms import SubscribersForm
# from .forms import SubscribersForm1


# Create your views here.

#
# def fn(request):
#     form = SubscribersForm(request.POST or None)
#     form1 = SubscribersForm1(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         new_form = form.save()
#     if request.method == "POST" and form1.is_valid():
#         new_form1= form1.save()
#     return render(request, 'ht.html',locals())


def test(request):
    return HttpResponse('1')
def test1(request):
    return HttpResponse('12')
def test2(request):
    return HttpResponse('123')