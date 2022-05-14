from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.



def caterers_booking(request):

    if request.method == "POST":

        forms = caterers_Form(request.POST)
        
        if forms.is_valid():

            forms.save()

        else:

            return render(request, 'caterers_booking.html', {"forms" : forms})

    
    else:

        forms = caterers_Form()

        
        return render(request, 'caterers_booking.html', {"forms" : forms})
    