from django.shortcuts import render



def index(request):

    return render(request, 'index.html')



def hotel_services(request):

    return render(request, 'hotel_services.html')

def restaurant_services(request):

    return render(request, 'restaurant_services.html')

def catering_services(request):

    return render(request, 'catering_services.html')

def lodging_services(request):

    return render(request, 'lodging_services.html')