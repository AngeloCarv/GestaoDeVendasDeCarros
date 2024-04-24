from django.contrib import admin
from cars.models import Car , BrandCars

class CarADM (admin.ModelAdmin):
    list_display = ('modelCar', 'brand', 'factory_year', 'value')
    search_fields = ('model',)

class brandADM (admin.ModelAdmin):
   list_display = ('name',)
   search_fields = ('name',)

admin.site.register(Car, CarADM)
admin.site.register(BrandCars, brandADM)