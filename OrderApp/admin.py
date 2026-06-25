from django.contrib import admin
from .models import Table,Catagory,MenuItem,Order,OrderItem,OrderHistory

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ["name","is_reserved"]
    
    
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name","default_priority"]


admin.site.register(Catagory)
admin.site.register(OrderItem)
admin.site.register(OrderHistory)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): 
    list_display = ["table","status","created_at"]
