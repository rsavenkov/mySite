from django.db import models

class Aklimenkostudent(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Aklimenkoperson(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
