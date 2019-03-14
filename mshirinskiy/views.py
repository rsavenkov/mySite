from django.http import HttpResponse
from django.template import loader

from mshirinskiy.models import Question_Mikle

def index(request):
    latest_question_list = Question_Mikle.objects.order_by('-pub_date')[:5]
    template = loader.get_template('mshirinskiy/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def mshirinskiy(request):
    return HttpResponse("Hey, buddy! Still alive?")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


