from django.contrib import admin

from .models import Address, Images, Category,HouseType, HouseFeatures, House

admin.site.register((Address, Images, Category,HouseType, HouseFeatures, House,))