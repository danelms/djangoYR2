from unittest.util import _MAX_LENGTH
from django.db import models

class Pet(models.Model):
    sexChoices = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=sexChoices, blank=True)
    age = models.IntegerField()
    submissionDate =models.DateTimeField()
    #Implements many to many relationship between Vaccine and Pet classes
    vaccinations = models.ManyToManyField('Vaccine', blank = True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
