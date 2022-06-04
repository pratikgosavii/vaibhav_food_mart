from math import prod
from multiprocessing import context
from re import U
from django.http import JsonResponse
from django.shortcuts import redirect, render
from numpy import place
from .models import *
from .forms import *

from account.models import *

# Create your views here.



def view_store(request):

    data = product.objects.all()

    return render(request, 'store.html', {'data' : data})



def add_to_cart(request):


    if request.method == "POST":

        print('here')

        qty = request.POST.get('qty')
        unit_id = request.POST.get('unit_id')

        print(unit_id)

        if unit_id:

            unit_instance = product_unit.objects.get(id = unit_id)
            product_instance = unit_instance.product

        else:

            product_id = request.POST.get('product_id')
            product_instance = product.objects.get(id = product_id)
            unit_instance = product_unit.objects.get(product = product_instance)
        

        print(unit_instance)
        print(product_instance)
        print(qty)

        try:
            
            try:
                a = cart.objects.get(product = product_instance, user = request.user, unit = unit_instance)
                a.qty = qty
                a.save()
                return JsonResponse({'result' : True})
            except cart.DoesNotExist:
                print('here')
                a = cart.objects.create(product = product_instance, qty = qty, user = request.user, unit = unit_instance)
                return JsonResponse({'result' : True})
                

        except:
            print('here')
            return JsonResponse({'result' : False})
    
def view_cart(request):

    cart_data = cart.objects.filter(user = request.user)


    total_items = cart_data.count()

    cart_price = 0
    for i in cart_data:
        cart_price = cart_price + i.product.price


    address_data = address.objects.filter(user = request.user)

    context = {
        'data' : cart_data,
        'total_items' : total_items,
        'cart_price' : cart_price,
        'address_data' : address_data,
        'cart_data' : cart_data
    }

    return render(request, 'cart.html', context)


def delete_from_cart(request, cart_id):


    cart.objects.get(id = cart_id).delete()
    

    return redirect('cart')



from django.core import serializers

# assuming obj is a model instance


def product_option(request):

    product_id = request.POST.get('product_id')

    product_instance = product.objects.get(id = product_id)

    data = product_unit.objects.filter(product = product_instance)

    serialized_obj = serializers.serialize('json', data, use_natural_foreign_keys=True)

    return JsonResponse({ 'result' : serialized_obj})


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

def admin_orders_page(request):

    orders_data = placeorder.objects.all()

    return render(request, 'admin_orders_page', {'orders_data': orders_data})


def ajax_admin_orders_page(request, order_id):

    orders_data = placeorder.objects.get(id = order_id)

    status = request.POST.get('status')

    orders_data.status = status

    return JsonResponse({ 'result' : True})
