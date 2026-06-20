from django.shortcuts import render
from .decoraters import role_required
from AccountApp.models import User
from .models import Table


# Create your views here.
@role_required([User.ROLE_CHOICES.WAITER])
def tables_view(request):
    tables = Table.objects.all()
    
    return render(request, 'OrderApp/tables.html',{
        'tables':tables
    })

