from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('a', views.a, name = 'index'),
    path('b', views.b, name = 'index'),
    path('c', views.c),
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]