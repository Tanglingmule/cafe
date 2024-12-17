from django.contrib import admin
from .models import MenuItem, Customer, Order

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('forename', 'surname', 'email', 'balance')
    search_fields = ('forename', 'surname', 'email')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date')
    list_filter = ('order_date',)
    search_fields = ('customer__forename', 'customer__surname')
