from django.test import TestCase

from account.models import User

from ..models import Car, Delivery, Orders, PriceList
from ..utils.samples import (create_sample_car, create_sample_delivery,
                             create_sample_orders, create_sample_price_list)


class TestCarModel(TestCase):

    def test_car_creation(self):
        car = create_sample_car()
        self.assertTrue(isinstance(car, Car))


class TestPriceListModel(TestCase):

    def test_price_list_creation(self):
        price_list = create_sample_price_list()

        self.assertTrue(isinstance(price_list, PriceList))
        self.assertTrue(isinstance(price_list.car, Car))
        self.assertTrue(isinstance(price_list.delivery, Delivery))


class TestOrdersModel(TestCase):

    def test_order_creation(self):
        order = create_sample_orders()

        self.assertTrue(isinstance(order, Orders))
        self.assertTrue(isinstance(order.client, User))
        self.assertTrue(isinstance(order.price_list, PriceList))


class TestDeliveryModel(TestCase):

    def test_delivery_creation(self):
        delivery = create_sample_delivery()

        self.assertTrue(isinstance(delivery, Delivery))
