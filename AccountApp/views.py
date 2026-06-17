from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def login_view(request):
     if request.method =="POST":
          username = request.POST.get("username")
          password = request.POST.get("password")
          user = authenticate(request,username=username,password=password)
          remember_me = request.POST.get("remember_me")
          # print(user)
          if user is not None:
             login(request,user)
             messages.success(request,"Login Successful")
          #    print("Log in successfull")
             if remember_me is None:
                request.session.set_expiry(0)

             return redirect('tables_view_url')
          else:
               messages.error(request,"Invalid Credentials")
               return redirect("login_view_url")

              
    
     return render(request, 'AccountApp/login_page.html')