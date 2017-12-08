from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Goods)
admin.site.register(Customer)
admin.site.register(GoodType)
admin.site.register(ShoppingCar)
admin.site.register(Manager)
