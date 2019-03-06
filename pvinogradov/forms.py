from django import forms
from .models import *


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        exclude = [""]
class SubscribersForm1(forms.ModelForm):
    class Meta:
        model = Subscribers1
        exclude = [""]

class SubscribersForm2(forms.ModelForm):
    class Meta:
        model = Subscribers2
        exclude = [""]
class SubscribersForm3(forms.ModelForm):
    class Meta:
        model = Subscribers3
        exclude = [""]
