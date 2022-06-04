from django.http import JsonResponse
from django.shortcuts import render

from rooms.models import room_book
from .forms import *
from store.models import *
# Create your views here.




def account(request):

    orders_data = placeorder.objects.filter(user = request.user)
    booking_data = room_book.objects.all()

    context = {
        'orders_data' : orders_data,
        'booking_data' : booking_data
    }

    return render(request, 'accounts.html', context)





from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate 

def login_user(request):

    if request.method == "POST":
        print('in post')
       
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {email}.")
            return redirect("index")
        
        else:
            messages.error(request,"Invalid email or password.")
    form = NewUserForm()
    return render(request=request, template_name="login.html", context={"login_form":form})


def signup(request):
    if request.method == "POST":
        print(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("login")
        else:
            print(form.errors)
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request, "signup.html", context={"register_form":form})




def add_address(request):

    if request.method == "POST":

        print('here')


       
        post = request.POST.copy() 
        post.update({"user": request.user})
        request.POST = post
        forms = address_Form(request.POST)

        if forms.is_valid():
            forms.save()

            return JsonResponse({'result' : True})
            
        else:
            return render(request, 'show_address.html', {'forms' : forms})

    else:
        

        return render(request, 'show_address.html')


def show_address(request):

    if request.method == "POST":

        address_id = request.POST.get('address_id')

        request.session['address_id'] = address_id

        return redirect('placeorder')

    else:
            
        address_data = address.objects.filter(user = request.user)

        return render(request, 'show_address.html', {'address': address_data})



