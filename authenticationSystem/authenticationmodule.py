from django.contrib.auth import authenticate, login, logout
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
        newuser = User()
    return render(request, 'Auth/signup.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'Auth/login.html')

