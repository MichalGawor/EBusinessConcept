import django
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField
from djmoney.models.fields import MoneyField
from datetime import datetime
import requests

class Entity(models.Model):
    EntityID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, default='')
    Surname = models.CharField(max_length=200, default='')
    Email = models.CharField(max_length=200, default='')
    Phone = models.IntegerField(default=0)
    BranchName = models.CharField(max_length=200, default='')

    def __str__(self):
       return self.Name + " " + self.Surname


class AlcoholType(models.Model):
    TypeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, default='')
    Taxation = models.IntegerField(default=0)

    def __str__(self):
       return self.Name




class Shop(models.Model):
    ShopID = models.AutoField(primary_key=True)
    EntityID = models.ForeignKey(Entity, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200, default='')
    Addres = models.CharField(max_length=200, default='')
    BranchName = models.CharField(max_length=200, default='')

    def __str__(self):
       return self.Name

CONTAINERS = (
    ('1', 'Bottle'),
    ('2', 'Can'),
    ('3', 'Box'),
    ('4', 'Bag')
)

class Alcohol(models.Model):
    AlchoholID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, default='')
    Volume = models.IntegerField(default=0)
    Percentage = models.IntegerField(default=0)
    Container = models.CharField(default='Bottle', max_length=10, choices=CONTAINERS)
    TypeID = models.ForeignKey(AlcoholType, on_delete=models.CASCADE)



    def __str__(self):
       return self.Name + str(self.Volume)




class Offer(models.Model):
    OfferID = models.AutoField(primary_key=True)
    ShopID = models.ForeignKey(Shop, on_delete=models.CASCADE)
    DateFrom = models.DateField(default=datetime.now)
    DateTo = models.DateField(default=datetime.now)
    AlcoholID = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
    Amount = models.IntegerField(default=0)
    Price = MoneyField(max_digits=10, decimal_places=2, default_currency='PLN')
    Comment = models.CharField(max_length=2000, default='')

