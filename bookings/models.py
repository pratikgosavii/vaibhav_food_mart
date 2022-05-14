from pyexpat import model
from secrets import choice
from django.db import models
from django.forms import CharField

# Create your models here.

service_choice = (
    ('Preparations only', 'Preparations only'),
    ('Preparations/Transportation', 'Preparations/Transportation'),
    ('Preparation/Transportation/Staff', 'Preparation/Transportation/Staff'),
)

class caterers(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    mobile_no = models.IntegerField()
    service = models.CharField(choices=service_choice, max_length=100)
    

    def __str__(self):
        return self.name

