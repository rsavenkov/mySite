from django.db import models

class Truck(models.Model):
    model = models.CharField(max_length=200)
    distance = models.IntegerField(default=0)

    def __str__(self):
        return self.model

class Car(models.Model):
    model = models.CharField(max_length=200)
    distance = models.IntegerField(default=0)

    def __str__(self):
        return self.model
