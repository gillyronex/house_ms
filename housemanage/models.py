from django.db import models

# Create your models here.

class Owner(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    phone=models.PositiveBigIntegerField()

class House (models.Model):
    address=models.CharField(max_length=100)
    Owner=models.ForeignKey(Owner, on on_delete==models.)
    num_rooms=models.PositiveIntegerField()
    is_available=models.BooleanField(default=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)

class Tenant(models.model)
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    phone=models.PositiveBigIntegerField()
    house=models.ForeignKey(House, on_delete=models.CASCADE)
    