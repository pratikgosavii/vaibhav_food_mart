from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.




def rooms(request):

    data =  room.objects.all()

    return render(request, 'hotel_rooms.html', {'data' : data})


def book_room(request):

    import dateutil.parser

    room_id = request.POST.get('room')

    room_instance = room.objects.get(id = room_id)

    from datetime import datetime
    date_time1 = request.POST.get('from_date_time')

    d = dateutil.parser.parse(date_time1)
    from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

    date_time1 = request.POST.get('to_date_time')
    d = dateutil.parser.parse(date_time1)
    to_date_time = d.strftime("%Y-%m-%d %H:%M:%S")


    post = request.POST.copy() 
    post.update({"from_date_time" : from_date_time, "to_date_time" : to_date_time, "user": request.user, "room" : room_instance,})
    request.POST = post

    forms = room_book_Form(request.POST)
    
    if forms.is_valid():
        forms.save()

        return JsonResponse({'result' : True})


    else:

        print(forms.errors)

        return JsonResponse({'result' : False})




def test(request):

    adad = room_book.objects.last()

    adad = adad.from_date_time

    data =  room.objects.all()



    return render(request, 'hotel_rooms.html', {"daadadta" : adad, 'data' : data})