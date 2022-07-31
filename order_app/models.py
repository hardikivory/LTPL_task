from datetime import time, timedelta, timezone
from itertools import product
from django.utils import timezone
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Order(models.Model):
    
    timestamp = models.DateTimeField(auto_now_add= True)
    placed = models.BooleanField(default=False)
    total_price = models.IntegerField(default=0)
    total_qty = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class Product(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products', null=True, blank=True) 
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    qty = models.IntegerField(default=0)
    # img

    def __str__(self):
        return str(self.id)


    