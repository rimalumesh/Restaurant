from django.shortcuts import render
from .decoraters import role_required
from AccountApp.models import User
from .models import Table,Catagory



# Create your views here.
@role_required([User.ROLE_CHOICES.WAITER])
def tables_view(request):
    tables = Table.objects.all()
    
    return render(request, 'OrderApp/tables.html',{
        'tables':tables
    })

@role_required([User.ROLE_CHOICES.WAITER])
def menu_view(request,table_id):
    categories = Catagory.objects.all()
    return render(request, 'OrderApp/menu.html',{
        'categories':categories,
        'table_id': table_id
    })

