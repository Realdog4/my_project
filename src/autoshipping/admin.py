from django.contrib import admin

from .models import Car, Category, Delivery, Orders, PriceList

admin.site.register([Category, Car, Delivery, PriceList, Orders])
