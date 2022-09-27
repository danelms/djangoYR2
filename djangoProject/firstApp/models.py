from unittest.util import _MAX_LENGTH
from django.db import models

class Pet(models.Model):
    _sexChoices = [('M', 'Male'), ('F', 'Female')]
    _name = models.CharField(max_length=100)
    _submitter = models.CharField(max_length=100)
    _species = models.CharField(max_length=30)
    _breed = models.CharField(max_length=30, blank=True)
    _description = models.TextField()
    _sex = models.CharField(max_length=1, choices=_sexChoices, blank=True)
    _age = models.IntegerField()
    _submissionDate =models.DateTimeField()
    #Implements many to many relationship between Vaccine and Pet classes
    _vaccinations = models.ManyToManyField('Vaccine', blank = True)

class Vaccine(models.Model):
    _name = models.CharField(max_length=50)
