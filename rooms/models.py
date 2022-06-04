from datetime import datetime
from pyexpat import model
from django.db import models
from django.forms import CharField

from django.contrib.auth import get_user_model
from razorpay import Payment
User = get_user_model()


# Create your models here.




class room(models.Model):

    name = models.CharField(max_length=50)
    room_capacity = models.CharField(max_length=500)
    facilities = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/room')

    
    def __str__(self):
        return self.name


class room_book(models.Model):

    room = models.ForeignKey(room, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    from_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    to_date_time = models.DateTimeField(auto_now=False)
    mobile = models.IntegerField()
    total_bill = models.IntegerField()
    adults = models.IntegerField()
    children = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   

    
    def __str__(self):
        return self.name

