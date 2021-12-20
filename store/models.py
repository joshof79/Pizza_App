from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    username=models.OneToOneField(User, on_delete=models.CASCADE)
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phoneNumber=models.IntegerField()

class Food(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(decimal_places=2, max_digits=6)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
    	try:
    		url = self.image.url
    	except:
    		url = ''
    	return url


class Order(models.Model):
    customerNumber=models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True)
    paid=models.BooleanField(default=False)
    order_number=models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class OrderFood(models.Model):
    food=models.ForeignKey(Food, on_delete=models.SET_NULL, null= True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null= True)
    quantity=models.IntegerField(default=0)
