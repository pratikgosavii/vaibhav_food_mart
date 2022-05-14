from pyexpat import model
from random import choices
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.


from django.contrib.auth import get_user_model
from razorpay import Payment
User = get_user_model()



class product(models.Model):

    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media/product/images')
    unit = models.CharField(max_length=1000)
    price = models.IntegerField()
    dis = models.CharField( max_length=500)
    

    def __str__(self):
        return self.name

class cart(models.Model):

    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.IntegerField()
    

    def __str__(self):
        return self.product.name


class address(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name



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
        return self.name



