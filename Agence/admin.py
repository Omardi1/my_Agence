from django.contrib import admin
from Agence.models import Suite, Category, Order, Cart
# Register your models here.

  

admin.site.register(Category)
admin.site.register(Suite)
admin.site.register(Order)
admin.site.register(Cart)
