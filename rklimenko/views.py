from .models import Question, Choice, Rklimenkostudent, Rklimenkoperson
# from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def standart(request):
    return HttpResponse('Welcome to the match in an Emirates Stadium')

def rklim(request):
    return HttpResponse('Hello from Ruslan!!')

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'rklimenko/results.html', {'question': question})

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    students = Rklimenkostudent.objects.all()
    persons = Rklimenkoperson.objects.all()
    context = {'latest_question_list': latest_question_list,
               'students': students,
               'persons': persons
               }
    return render(request, 'rklimenko/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'rklimenko/detail.html', {'question': question})