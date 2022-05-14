

from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime



class product_Form(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'
       
       

class address_Form(forms.ModelForm):
    class Meta:
        model = address
        fields = '__all__'
       
       