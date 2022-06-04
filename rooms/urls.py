from django.urls import path

from .views import *


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [


    path('', rooms, name='rooms'),
    path('book-room', book_room, name='book_room'),
    path('test', test, name='test'),


]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)