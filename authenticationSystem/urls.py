from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views, authenticationmodule

urlpatterns = [

    path('', views.home),
    path('login/', authenticationmodule.login),
    path('signup/', authenticationmodule.signup),
]