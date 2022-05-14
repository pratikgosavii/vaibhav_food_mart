

from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime



class caterers_Form(forms.ModelForm):
    class Meta:
        model = caterers
        fields = '__all__'
       