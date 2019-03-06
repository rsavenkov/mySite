from django.db import models

class Rklimenkostudent(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Rklimenkoperson(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
