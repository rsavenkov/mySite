#from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from datetime import datetime

class Question_afrolov(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # def __str__(self):
    #     return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice_afrolov(models.Model):
    question = models.ForeignKey(Question_afrolov, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

class Metro(models.Model):
    train = models.CharField(max_length=200)