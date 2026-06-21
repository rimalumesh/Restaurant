from django.contrib import admin
from .models import Table,Catagory,MenuItem,Order,OrderItem

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ["name","is_reserved"]
    
admin.site.register(Catagory)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)