from django.contrib import admin
from customer.models import Customer
from customer.models import Students
from customer.models import Menu

admin.site.register(Customer)

admin.site.register(Students)
admin.site.register(Menu)

# Register your models here.
