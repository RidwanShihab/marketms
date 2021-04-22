from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'cms/dashboard.html',{'user':request.user})

def billing(request):

    # Redirect to a success page.
    return render(request, 'cms/billing.html')

def profile(request):

    # Redirect to a success page.
    return render(request, 'cms/profile.html')