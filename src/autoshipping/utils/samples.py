from datetime import datetime
import random

from django.utils.timezone import make_aware, timedelta

from account.models import User

from ..models import Car, Category, Delivery, Orders, PriceList

CATEGORY_NAMES = ["Passenger car", "SUV", "Truck", "Electric vehicle", "Luxury car"]


def generate_category():
    name = random.choice(CATEGORY_NAMES)
    return Category.objects.create(name=name)

def create_sample_car():
    categories = ["Sedan", "SUV", "Truck"]
    colors = ["Red", "Blue", "Black", "White"]

    category = Category.objects.create(name=random.choice(categories))
    car = Car.objects.create(
        category=category,
        name=f"Car {random.randint(1, 100)}",
        brand=f"Brand {random.randint(1, 10)}",
        model=f"Model {random.randint(1, 5)}",
        year=random.randint(2000, 2023),
        description="Sample description",
        vin_code=f"VIN{random.randint(10000000000000000, 99999999999999999)}",
        mileage=random.randint(0, 100000),
        color=random.choice(colors),
        price=random.randint(1000, 50000)
    )
    return car


def create_sample_delivery():
    delivery = Delivery.objects.create(
        delivery_date=make_aware(datetime.now()),
        distance=random.randint(50, 500),
        duration=timedelta(hours=random.randint(1, 5)),
        cost=random.randint(10, 100)
    )
    return delivery


def create_sample_price_list(car=None):
    if car is None:
        car = create_sample_car()
    delivery = create_sample_delivery()
    price_list = PriceList.objects.create(
        car=car,
        price=random.randint(1000, 50000),
        delivery=delivery
    )
    return price_list


def create_sample_orders(client=None, price_list=None):
    if client is None:
        client = User.objects.create_user(first_name="test_user_name",
                                          last_name="test_last_name", email="test@example.com",
                                          password="testpassword")
    if price_list is None:
        price_list = create_sample_price_list()
    order = Orders.objects.create(
        client=client,
        status=random.choice(["Pending", "Processing", "Completed"]),
        price_list=price_list
    )
    return order
