from django.urls import path

from .views import *


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('', view_store, name='view_store'),

    path('Add-to-cart/', add_to_cart, name='add_to_cart'),
    path('Cart/', view_cart, name='view_cart'),
    path('Delete-to-cart/', delete_from_cart, name='delete_from_cart'),
    
    path('product-option/', product_option, name='product_option'),



    path('placeorder', placeorder, name='placeorder'),

]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)