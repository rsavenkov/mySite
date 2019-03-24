from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader

from .models import Question_Mikle, Choice_Mikle, Act_Mikle

# def question(request):
#     latest_question_list = Question_Mikle.objects.order_by('-pub_date')[:5]
#     #template = loader.get_template('mshirinskiy/index.html')
#     #context = {
#         #'latest_question_list': latest_question_list,
#
#     # return HttpResponse(template.render(context, request))
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

def index(request):
    Question_Mike =  Question_Mikle.objects.all()
    Choice_Mike = Choice_Mikle.objects.all()
    context = {'Question_Mikle': Question_Mikle,
               'Choice_Mikle': Choice_Mikle,
               }
    return render(request, 'mshirinskiy/index.html', context)

def actmikle(request):
    latest_action =  Act_Mikle.objects.all()
    context = {'latest_action': latest_action,
               }
    return render(request, 'mshirinskiy/index2.html', context)


def submit(request):
    latest_action = Act_Mikle.objects.all() [0]
    return render(request, '/mshirinskiy/detail.html', {'action': latest_action})

def latest_action(request):
    HttpResponse('shoot')


def mshirinskiy(request):
    return HttpResponse("Hey, buddy! Still alive?")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


