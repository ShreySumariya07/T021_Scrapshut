from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    phone = models.FloatField(default=0.0)
    isDonar = models.BooleanField(default=False)
    isNGO = models.BooleanField(default=False)


class Donar(models.Model):
    user_donar = models.OneToOneField(
        User, on_delete=models.CASCADE, default="", related_name="profile")
    Address = models.TextField(max_length=1000, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.IntegerField()


class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    ngo_Address = models.TextField(max_length=1000, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.IntegerField()
    weblink = models.URLField()


class Equipments(models.Model):
    eqi_name = models.CharField(max_length=200)
    Price = models.FloatField()
    image = models.ImageField(default='')

    def __str__(self):
        return self.eqi_name


class Requirements(models.Model):
    ngoid = models.ForeignKey(User, on_delete=models.CASCADE)
    eqiid = models.ForeignKey(Equipments, on_delete=models.CASCADE)
    Quantity = models.IntegerField()


class Donations(models.Model):
    userid = models.ForeignKey(
        User, on_delete=models.CASCADE)
    ngoid = models.ForeignKey(
        NGO, on_delete=models.CASCADE)
    eqiid = models.ForeignKey(Equipments, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
