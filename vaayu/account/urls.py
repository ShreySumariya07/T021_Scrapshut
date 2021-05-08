from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'account'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('RegisterAsUser', views.RegisterAsUser, name="RegisterAsUser"),
    path('RegisterAsNgo', views.RegisterAsNgo, name="RegisterAsNgo"),
    path('LoginAsNgo', views.LoginAsNgo, name="LoginAsNgo"),
    path('LoginAsUser', views.LoginAsUser, name="LoginAsUser"),
    path('UserDonate/<int:user_id>/', views.UserDonate, name="UserDonate"),
    path('UserDonation/<int:user_id>/', views.UserDonation, name="UserDonation"),
    path('NgoRequirement/<int:user_id>/',
         views.NgoRequirement, name="NgoRequirement"),
    path('DonationSuccessful/<int:ngoid>/<int:user_id>/', views.DonationSuccessful,
         name="DonationSuccessful"),
    path('DonateUser/<int:ngo_id>/<int:user_id>/',
         views.DonateUser, name="DonateUser"),
    path('addNgoRequirement/<int:user_id>/',
         views.addNgoRequirement, name="addNgoRequirement"),
]
