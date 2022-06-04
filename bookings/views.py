from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.



def caterers_booking(request):

    if request.method == "POST":

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

            
        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post


        forms = caterers_Form(request.POST)
        
        if forms.is_valid():

            forms.save()

        else:
            
            print(forms.errors)
            return render(request, 'caterers_booking.html', {"forms" : forms})

    
    else:

        forms = caterers_Form()

        
        return render(request, 'caterers_booking.html', {"forms" : forms})
    


import dateutil.parser
def table_booking(request):

    if request.method == "POST":


        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

            
        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post


        forms = table_Form(request.POST)

        if forms.is_valid():

            forms.save()



        else:

            print(forms.errors)


    else:

        return render(request, 'table_booking.html', {})


def hotel_booking(request):

    if request.method == "POST":

        print(request.POST)

        forms = caterers_Form(request.POST)
        
        if forms.is_valid():

            forms.save()

        else:
            
            print(forms.errors)
            return render(request, 'hotel_rooms.html', {"forms" : forms})

    
    else:

        forms = caterers_Form()

        
        return render(request, 'hotel_rooms.html', {"forms" : forms})
    