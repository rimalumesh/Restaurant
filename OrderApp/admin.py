from django.contrib import admin
from .models import Table,Catagory,MenuItem,Order,OrderItem,OrderHistory

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ["name","is_reserved"]
    
admin.site.register(Catagory)
admin.site.register(MenuItem)
admin.site.register(OrderItem)
admin.site.register(OrderHistory)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): 
    list_display = ["table","status","created_at"]
