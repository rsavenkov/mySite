from django.shortcuts import render

# Create your views here.

from afrolov.models import Question_afrolov, Choice_afrolov
from django.shortcuts import render


def index(request):
    latest_question_list = Question_afrolov.objects.order_by('-pub_date')[:5]
    latest_choice_list = Choice_afrolov.objects.all()
    context = {'latest_question_list': latest_question_list,
               'latest_choice_list': latest_choice_list}
    return render(request, 'afrolov/index.html', context)

