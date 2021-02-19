from django.db import models

class Zodiac(models.Model):
    entry_time = models.DateTimeField()
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    point = models.CharField(max_length=100)
    zodiac = models.CharField(max_length=100)
    z_longitude = models.FloatField()
    house = models.IntegerField()
    RA = models.FloatField()

class Aspects(models.Model):
    entry_time = models.DateTimeField()
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    body1 = models.CharField(max_length=100)
    body2 = models.CharField(max_length=100)
    shape = models.IntegerField()
    degree_type = models.FloatField()
    degree = models.FloatField()

class User_info(models.Model):
    entry_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    hour =  models.IntegerField()
    minute =models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    natal_chart = models.ImageField(default='default.png', blank=True)
    aspect_grid = models.ImageField(default='default.png', blank=True)