from django.contrib import admin
from django.urls import path
from django.urls import include

from authenticationSystem import cms
from . import views, authenticationmodule

urlpatterns = [

    path('', views.home),
    path('login/', authenticationmodule.userlogin, name='loginpage'),
    path('signup/', authenticationmodule.signup, name='signuppage'),
    path('dashboard/', cms.dashboard, name='dashboardpage'),
    path('logout/', authenticationmodule.logout_view, name='logoutpage'),
]