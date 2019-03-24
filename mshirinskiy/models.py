from django.db import models
from django.utils import timezone
from _datetime import datetime

class Mikle(models.Model):
    pass

class Question_Mikle(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text




class Choice_Mikle(models.Model):
    question = models.ForeignKey(Question_Mikle, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Act_Mikle(models.Model):
    act_on_instinct = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.act_on_instinct, self.pub_date


