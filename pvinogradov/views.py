from django.shortcuts import render
from .forms import SubscribersForm
from .forms import SubscribersForm1
from .forms import SubscribersForm2


# Create your views here.


def fn(request):
    form = SubscribersForm(request.POST or None)
    form1 = SubscribersForm1(request.POST or None)
    form2 = SubscribersForm2(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    if request.method == "POST" and form1.is_valid():
        new_form1= form1.save()
    if request.method == "POST" and form2.is_valid():
        new_form2= form2.save()

    return render(request, 'ht.html', locals())


