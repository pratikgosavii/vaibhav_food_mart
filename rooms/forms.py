

from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime



class room_book_Form(forms.ModelForm):
    class Meta:
        model = room_book
        fields = '__all__'
       