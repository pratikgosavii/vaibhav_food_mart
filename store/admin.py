from django.contrib import admin
from .models import *

# Register your models here.



admin.site.register(product)
admin.site.register(cart)
admin.site.register(product_unit)
admin.site.register(placeorder)