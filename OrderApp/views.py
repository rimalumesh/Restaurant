from django.shortcuts import render,redirect
from .decoraters import role_required
from AccountApp.models import User
from .models import Table,Catagory,Order,OrderItem,MenuItem,KitchenStation
import json
from django.contrib import messages
from django.http import HttpResponse
from . import signals


# Create your views here.
@role_required([User.ROLE_CHOICES.WAITER])
def tables_view(request):
    tables = Table.objects.all()
    
    return render(request, 'OrderApp/tables.html',{
        'tables':tables
    })

@role_required([User.ROLE_CHOICES.WAITER])
def menu_view(request,table_id):
    if request.method == "POST":
        data = request.POST.get("order-items")
        data_dict = json.loads(data)
        print(data_dict,type(data_dict))
        
        table_id = data_dict.get('table_id')
        table_obj = Table.objects.get(pk= table_id)
        order = Order.objects.create(
            table = table_obj
        )
        
        for orderitem in data_dict.get('items'):
            menu_item = MenuItem.objects.get(pk=orderitem.get('item_id'))
            OrderItem.objects.create(
                order = order,
                menu_item = menu_item,
                price = menu_item.price,
                quantity = orderitem.get('quantity'),
                priority = menu_item.default_priority      
            )
        messages.success(request,"Order Created Successfully")
        return redirect("tables_view_url")
    
    categories = Catagory.objects.all()
    orders = Order.objects.filter(table_id=table_id).exclude(status = Order.ORDER_STATUS.BILLED).order_by('-created_at')
    
    return render(request, 'OrderApp/menu.html',{
        'categories':categories,
        'table_id': table_id,
        'orders': orders
    })


@role_required([User.ROLE_CHOICES.KITCHEN])
def kitchen_dashboard_view(request):
    orderitems = OrderItem.objects.all().order_by("-priority")
    grouped_items = {}
    
    for item in orderitems:
        station_name = item.menu_item.station.name
        if station_name not in grouped_items.keys():
            grouped_items[station_name] = [item]
        else:
            grouped_items[station_name].append(item)
    stations = KitchenStation.objects.all()
    return render(request, 'OrderApp/kitchen_dashboard.html',{
        'order_items': grouped_items
    })

