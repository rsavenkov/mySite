from django.urls import path

from . import views

urlpatterns = [
    path('msh', views.mshirinskiy, name='mshirinskiy'),
    # ex: /polls/
    path('q', views.question, name='question'),
    # ex: /polls/5/
    path('c', views.choice, name='choice'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]