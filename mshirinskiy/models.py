from django.db import models

class Mikle(models.Model):
    pass

class Question_Mikle(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')




class Choice_Mikle(models.Model):
    question = models.ForeignKey(Question_Mikle, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
