from django.db import models

class Street(models.Model):
    street_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class House(models.Model):
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)