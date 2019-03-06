from django.db import models

# Create your models here.
class Subone(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)

class Subtwo(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)