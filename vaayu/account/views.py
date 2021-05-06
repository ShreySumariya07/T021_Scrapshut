
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .forms import *
from .models import *



# Create your views here.
def index(request):
    return render(request,"index.html")

def RegisterAsUser(request):
    if request.method == "POST":
        username = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        country = request.POST.get('country')
        pincode = request.POST.get('pincode')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2:
            if User.objects.filter(username = username).exists():
                messages.error(request,"username taken")
                return redirect('register-donor.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"email already taken")
                return redirect('register-donor.html')
            else:
                user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,phone=phone,isDonar=True,isNGO=False)
                donor = Donar.objects.create(user_donar=user,Address=address,country=country,pincode=pincode)
                user.save()
                donor.save
                return redirect('account:LoginAsUser')
        else:
            messages.error(request,"incorrect password")
            return redirect('register-donor-html')
    else:
        messages.info(request,"invalid error")
        return render(request,"register-donor.html")

def RegisterAsNgo(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        country = request.POST.get('country')
        pincode = request.POST.get('pincode')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        weblink = request.POST.get('weblink')
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username taken")
                return redirect('register-donor.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "email already taken")
                return redirect('register-donor.html')
            else:
                user = User.objects.create_user(username=username, email=email, first_name=first_name, phone=phone, isDonar=True, isNGO=False)
                ngo = NGO.objects.create(user_ngo=user, ngo_Address=address, country=country, pincode=pincode,weblink=weblink)
                user.save()
                ngo.save
                return redirect('account:LoginAsNgo')
        else:
            messages.error(request, "incorrect password")
            return redirect('register-ngo-html')
    else:
        messages.info(request, "invalid error")
        return render(request, "register-ngo.html")


def LoginAsUser(request):
    if request.method == 'POST':
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        if user is  None:
            return render(request,"userdonation.html")
        else:
            messages.error(request,"invalid username or password")
            return render(request,"login.html")
    else:
        return render(request, "login.html")

def LoginAsNgo(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        if user is None:
            return render(request,"homepagelogin.html")
        else:
            messages.error(request,"invalid username or password")
            return render(request,"login-ngo.html")
    else:
        return render(request, "login-ngo.html")

def RegisterAsUserSuccess(request):
    return render(request,"userdonation.html")

def UserDonation(request):
    return render(request,"donated items.html")

def NgoHomePage(request):
    return render(request,"homepagelogin.html")

def about(request):
    return render(request,"about.html")

def NgoRequirement(request):
    equipments = Equipments.objects.all()
    equi_dict = {'Equipments': equipments}
    return render(request,"request.html",equi_dict)

def DonateUser(request):
    equipments = Equipments.objects.all()
    equi_dict = {'Equipments': equipments}
    return render(request, "donation.html", equi_dict)