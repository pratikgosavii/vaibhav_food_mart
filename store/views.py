from math import prod
from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import redirect, render
from numpy import place
from .models import *
from .forms import *

# Create your views here.

def add_to_cart(request):


    if request.method == "POST":

        product_id = request.POST.get('product_id')
        qty = request.POST.get('qty')

        product_instance = product.objects.get(id = product_id)

        try:
            cart.objects.create(product = product_instance, qty = qty)
            return JsonResponse({'result' : True})

        except:
            return JsonResponse({'result' : False})
    
def view_cart(request):

    cart_data = cart.objects.filter(user = request.user)


    total_items = cart_data.count()

    cart_price = 0
    for i in total_items:
        cart_price = cart_price + i.price

    context = {
        'data' : cart_data,
        'total_items' : total_items,
        'cart_price' : cart_price
    }

    return render(request, 'cart.html', context)


def delete_from_cart(request, cart_id):


    cart.objects.get(id = cart_id).delete()
    

    return redirect('cart')



def placeorder(request):

    if request.method == "POST":

        cart_data = cart.objects.filter(user = request.user)

        total_price = 0

        for i in cart_data:
            total_price = total_price + (i.product.price * i.qty)

        if request.session['address_id'] != None:
            print('please add address')
            return redirect('show_address')

        address_id = request.session['address_id']
        address_instance = address.objects.get(id = address_id)

        payment_type = 'cash on delivery'

        for i in cart_data:
            
            try:
                placeorder.objects.create(user = request.user, product = i.product, address = address_instance, payment = payment_type, status = 'recived')
            except:
                print('something went wrong')

        return render(request, 'order_successful.html')

    else:

        return render(request, 'placeorder1.html')

def add_address(request):

    if request.method == "POST":

        forms = address_Form(request.POST)

        if forms.is_vaild():
            forms.save()
            
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




def admin_orders_page(request):

    orders_data = placeorder.objects.all()

    return render(request, 'admin_orders_page', {'orders_data': orders_data})




def ajax_admin_orders_page(request, order_id):

    orders_data = placeorder.objects.get(id = order_id)

    status = request.POST.get('status')

    orders_data.status = status

    return JsonResponse({ 'result' : True})