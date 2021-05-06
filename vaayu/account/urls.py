from django.contrib import admin
from django.urls import path
from . import  views

app_name = 'account'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('RegisterAsUser',views.RegisterAsUser,name = "RegisterAsUser"),
    path('RegisterAsNgo',views.RegisterAsNgo,name = "RegisterAsNgo"),
    path('LoginAsNgo',views.LoginAsNgo,name = "LoginAsNgo"),
    path('LoginAsUser',views.LoginAsUser,name="LoginAsUser"),
    path('UserDonation',views.UserDonation,name="UserDonation"),
    path('NgoRequirement',views.NgoRequirement,name="NgoRequirement"),
    path('NgoHomepage',views.NgoHomePage,name = "NgoHomepage"),
    path('RegisterAsUserSuccess',views.RegisterAsUserSuccess,name="RegisterAsUserSuccess"),
    path('DonateUser',views.DonateUser,name="DonateUser"),
]
