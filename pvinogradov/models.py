from django.db import models


class Subscribers(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()


class Subscribers1(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)


class Subscribers2(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    article_imge = models.ImageField(null=True, blank=True, upload_to='media  ', verbose_name='ww.jpg')

class Subscribers3(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    article_imge = models.ImageField(null=True, blank=True, upload_to='media  ', verbose_name='ww.jpg')

    # name = models.CharField(max_length=128)
    # data = models.DateField(1)
