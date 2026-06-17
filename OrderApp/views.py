from django.shortcuts import render

# Create your views here.
def tables_view(request):
    return render(request, 'OrderApp/tables.html')
    