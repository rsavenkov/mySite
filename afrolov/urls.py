from django.urls import path

from . import views

urlpatterns = [
    path('example1', views.example1),
    path('example2', views.example2),
    # path('afrolov', views.afrolov, name='afrolov'),
# ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]