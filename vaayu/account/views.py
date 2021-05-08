from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


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
            if User.objects.filter(username=username).exists():
                messages.error(request, "username taken")
                return redirect('register-donor.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "email already taken")
                return redirect('register-donor.html')
            else:
                user = User.objects.create_user(
                    username=username, email=email, first_name=first_name, last_name=last_name, phone=phone, isDonar=True, isNGO=False)
                donor = Donar.objects.create(
                    user_donar=user, Address=address, country=country, pincode=pincode)
                user.save()
                donor.save
                return redirect('account:LoginAsUser')
        else:
            messages.error(request, "incorrect password")
            return redirect('register-donor-html')
    else:
        messages.info(request, "invalid error")
        return render(request, "register-donor.html")


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
                user = User.objects.create_user(
                    username=username, email=email, first_name=first_name, phone=phone, isDonar=False, isNGO=True)
                ngo = NGO.objects.create(
                    user_ngo=user, ngo_Address=address, country=country, pincode=pincode, weblink=weblink)
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
        user = auth.authenticate(username=username, password=password)
        if user is None:
            user = User.objects.get(username=username)
            return render(request, "donarhomepage.html", {"user": user})
        else:
            messages.error(request, "invalid username or password")
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def LoginAsNgo(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is None:
            user = User.objects.get(username=username)
            print(user)
            return render(request, "homepagelogin.html", {"user": user})
        else:
            messages.error(request, "invalid username or password")
            return render(request, "login-ngo.html")
    else:
        return render(request, "login-ngo.html")


def DonationSuccessful(request, ngoid, user_id):
    if request.method == 'POST':
        nid = User.objects.get(id=ngoid)
        ngid = NGO.objects.get(user_id=nid.id)
        print(ngid.id)
        user = User.objects.get(id=user_id)
        usid = User.objects.only("id").get(id=user_id)
        equipments = Equipments.objects.all()
        for equip in equipments:
            quantity = int(request.POST.get('{}'.format(equip.id)))
            if quantity > 0:
                donation = Donations.objects.create(
                    userid=usid, ngoid=ngid, eqiid=equip, Quantity=quantity)
                donation.save()
            else:
                continue
        return render(request, "donarhomepage.html", {"user": user})
    else:
        user = User.objects.get(id=user_id)
        messages.error(request, "invalid method")
        return render(request, "donarhomepage.html", {"user": user})


def UserDonate(request, user_id):
    user = User.objects.get(id=user_id)
    ngo = User.objects.filter(isNGO=True)
    l = []
    for i in ngo:
        id = i.id
        ngorequire = Requirements.objects.filter(
            ngoid=id).values("Quantity", "eqiid")
        v = []
        for ngid in ngorequire:

            nid = ngid.get("eqiid")
            nquantity = ngid.get("Quantity")
            print(nquantity)
            print(nid)
            equiname = Equipments.objects.get(id=nid)
            dic = {equiname.eqi_name: nquantity}
            v.append(dic)
        detail = {i: v}
        l.append(detail)
    print(l)
    return render(request, 'userdonation.html', {"user": user, 'l': l})


def UserDonation(request, user_id):
    l = []
    ngid = NGO.objects.filter(user_id=user_id).values("id")
    for ngd in ngid:
        nid = ngd.get("id")
    equipment = Equipments.objects.all()
    vi = []
    for equip in equipment:
        donation = Donations.objects.filter(eqiid=equip.id)
        # user = User.objects.get(id=donation.userid_id)
        v = {
            "user": user,
            "ngoid": donation.ngoid_id,
            "Quantity": donation.Quantity,
        }
        vi.append(v)
    detail = {equip.eqi_name: vi}
    l.append(detail)
    print(l)
    return render(request, "donated items.html", {"equipments": equipment, "l": l})


def about(request):
    return render(request, "about.html")


def NgoRequirement(request, user_id):
    equipments = Equipments.objects.all()
    user = User.objects.get(id=user_id)
    return render(request, "request.html", {"Equipments": equipments, "user": user})


def addNgoRequirement(request, user_id):

    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        usid = User.objects.only("id").get(id=user_id)
        equipments = Equipments.objects.only("id").all()
        for equip in equipments:
            quantity = request.POST.get('{}'.format(equip.id))
            print(quantity)
            requirement = Requirements.objects.create(
                ngoid=usid, eqiid=equip, Quantity=quantity)
            requirement.save()
        return render(request, "homepagelogin.html", {"user": user})
    else:
        return render(request, "request.html", {"equipments": equipments, "user": user})


def DonateUser(request, ngo_id, user_id):
    ngo = User.objects.get(id=ngo_id)
    user = User.objects.get(id=user_id)
    equipments = Equipments.objects.all()
    return render(request, "donation.html", {"Equipments": equipments, 'ngo': ngo, 'user': user})
