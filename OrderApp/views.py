from django.shortcuts import render
from .decoraters import role_required
from AccountApp.models import User


# Create your views here.
@role_required([User.ROLE_CHOICES.WAITER])
def tables_view(request):
    return render(request, 'OrderApp/tables.html')
    