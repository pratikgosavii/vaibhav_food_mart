from pyexpat import model
from random import choices
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.


from django.contrib.auth import get_user_model
from razorpay import Payment
User = get_user_model()

from account.models import *



class product(models.Model):

    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media/product/images')
    price = models.IntegerField()
    dis = models.CharField( max_length=500)
    

    def __str__(self):
        return self.name

    
    def natural_key(self):
        return (self.name)

class product_unit(models.Model):

    product = models.ForeignKey(product,related_name="unit_details",  on_delete=models.CASCADE)
    unit = models.CharField(max_length=1000)
    price = models.IntegerField()


    def __str__(self):
        return self.product.name

    def natural_key(self):
        return (self.product.name)



class cart(models.Model):

    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.IntegerField()
    unit = models.ForeignKey(product_unit, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.product.name




payment_choice = (
    ('online' , 'Online'),
    ('cash on delivery' , 'Cash on delivery'),
)

status_choice = (
    ('recived' , 'Recived'),
    ('accepted' , 'Accepted'),
    ('preparing' , 'Preparing'),
    ('out for delievry' , 'Out for delievry'),
    ('accepted' , 'Deliverd'),
    ('cancled' , 'Cancled'),
)


class placeorder(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'kjdjis')
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name= 'sdsd')
    address = models.ForeignKey(address, on_delete=models.CASCADE, related_name= 'sdsdsds')
    payment =  models.CharField(choices=payment_choice, max_length=100)
    status =  models.CharField(choices=status_choice, max_length=100)
    

    def __str__(self):
        return self.status



