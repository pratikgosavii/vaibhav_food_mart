from django.urls import path

from .views import *


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('', account, name='account'),
    path('login/', login_user, name='login'),
    path('register/', signup, name='signup'),

    
    path('Add-address/', add_address, name='add_address'),
    path('Show-address/', show_address, name='show_address'),



]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)