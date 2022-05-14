from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.



def caterers_booking(request):

    if request.method == "POST":

        print(request.POST)

        forms = caterers_Form(request.POST)
        
        if forms.is_valid():

            forms.save()

        else:
            
            print(forms.errors)
            return render(request, 'caterers_booking.html', {"forms" : forms})

    
    else:

        forms = caterers_Form()

        
        return render(request, 'caterers_booking.html', {"forms" : forms})
    