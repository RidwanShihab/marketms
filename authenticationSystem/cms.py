from django.shortcuts import render

# Create your views here.
from authenticationSystem.models import apply, bill


def dashboard(request):
    return render(request, 'cms/dashboard.html',{'user':request.user})

def billing(request):
    if request.method == "POST":

        b = bill()
        b.biller= request.user
        b.method =  request.POST.get('method')
        b.tid = request.POST.get('tid')
        b.phone = request.POST.get('phone')
        b.email = request.POST.get('email')
        b.amount = request.POST.get('amount')
        b.month = request.POST.get('month')
        b.stat = 'pending'
        b.save()

    billtable = bill.objects.filter(biller=request.user)



    # Redirect to a success page.
    return render(request, 'cms/billing.html',{'billtable':billtable})

def profile(request):

    # Redirect to a success page.
    return render(request, 'cms/profile.html')

def applyshop(request):

    # Redirect to a success page.

    if request.method == "POST":
        description =  request.POST.get('description')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        shopname = request.POST.get('shopname')
        recommender = request.POST.get('recommender')

        request.user.email = email
        request.user.profile.email = email
        request.user.save()
        applier= apply()
        applier.details=description
        applier.email=email
        applier.phone_number=phone
        applier.address=address
        applier.shopname=shopname
        applier.recommender=recommender
        applier.save()


    return render(request, 'cms/applyshop.html')




