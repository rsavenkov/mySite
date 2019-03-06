from django.db import models


class Subscribers(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()


class Subscribers1(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)


