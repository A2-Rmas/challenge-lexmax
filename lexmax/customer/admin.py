from django.contrib import admin

from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'lastname', 
        'email', 
        'address', 
        'reference_address', 
        'phone'
    ]
    list_filter = [
        'created_at'
    ]
    search_fields = [
        'name', 
        'lastname', 
        'email', 
        'address', 
        'reference_address', 
        'phone'
    ]
