from django.db import models
from django.utils import timezone

from account.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    description = models.TextField()
    vin_code = models.CharField(max_length=17, unique=True)
    mileage = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    delivery_date = models.DateTimeField(default=timezone.now)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Delivery {self.delivery_date}"


class PriceList(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car.name} - Price: {self.price}, Delivery: {self.delivery.cost}"


class Orders(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client} - {self.price_list.car.name}"
