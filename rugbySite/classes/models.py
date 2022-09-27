from email.policy import default
from django.db import models

class Player(models.Model):
    _name = models.CharField(max_length=100)
    _specialist = models.BooleanField('Specialist', default=False)
    _positions = models.ManyToManyField('Position', blank = True)

class Position(models.Model):
    _specialistPosition = models.BooleanField('Specialist Postion', default=False)
    _name = models.CharField(max_length=30)
