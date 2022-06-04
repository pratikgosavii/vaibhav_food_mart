from django.urls import path

from .views import *


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [



    # path('table-booking', table_booking, name='table_booking'),
    # path('room-booking', room_booking, name='room_booking'),
    path('caterers-booking', caterers_booking, name='caterers_booking'),
    path('table-booking', table_booking, name='table_booking'),

]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)