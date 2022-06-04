"""vaibhva_foods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name="index"),
    path('hotel-services', hotel_services, name="hotel_services"),
    path('restaurant-services', restaurant_services, name="restaurant_services"),
    path('catering-services', catering_services, name="catering_services"),
    path('lodging-services', lodging_services, name="lodging_services"),
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('bookings/', include('bookings.urls')),
    path('rooms/', include('rooms.urls')),
    path('account/', include('account.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)