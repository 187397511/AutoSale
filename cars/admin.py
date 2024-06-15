from django.contrib import admin
from .models import Car
# Register your models here.
class car_admin(admin.ModelAdmin):
    list_display = ('id', 'car_title', 'fuel_type', 'price', 'model', 'is_featured')
    list_display_links = ('id', 'car_title')
    search_fields = ('passengers', 'car_title', 'fuel_type', 'price', 'model')
    list_filter= ('fuel_type', 'is_featured')
    list_editable=('is_featured',)

admin.site.register(Car, car_admin)
