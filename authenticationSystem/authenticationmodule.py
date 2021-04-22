from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def userlogin(request):
    if request.method== "POST":
        user=authenticate(request, username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            return redirect('dashboardpage')
        else :
            return redirect('loginpage')

    return render(request, 'Auth/login.html')





def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone= request.POST.get('phone')
        password = request.POST.get('pasword')
        rpassword = request.POST.get('re_pasword')


        if password == rpassword :

            newUser = User()
            newUser.username = name
            newUser.phone = phone
            newUser.password = make_password(password)
            newUser.save()
            user = authenticate(request, username=request.POST.get('user_name'), password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('loginPage')




    return render(request, 'Auth/signup.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('loginpage')

