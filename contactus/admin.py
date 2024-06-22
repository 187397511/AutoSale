from django.contrib import admin
from .models import Contact
# Register your models here.
class Contact_admin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name', 'car_title', 'email', 'customer_needs')
    list_display_links = ('id', 'car_title', 'email')
    search_fields = ('first_name','last_name','email', 'car_title', 'customer_needs', 'state')
    list_filter= ('state', 'customer_needs')

admin.site.register(Contact, Contact_admin)
