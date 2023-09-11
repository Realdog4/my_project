from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED)
from rest_framework.test import APIClient

from autoshipping.models import Car
from autoshipping.utils.samples import create_sample_car


class CarAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(email="test_api@example.com")
        self.user.set_password("qwerty1234")
        self.user.save()

    def test_car_list_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/cars/')
        self.assertEqual(response.status_code, HTTP_200_OK)

    # def test_car_create_view(self):
    #     self.client.force_authenticate(user=self.user)
    #     data = {
    #         'category': 1,
    #         'name': 'Toyota Camry',
    #         'brand': 'Toyota',
    #         'model': 'Camry',
    #         'year': 2022,
    #         'description': 'Toyota Camry',
    #         'vin_code': 'JTNB11HK102345678',
    #         'mileage': 15000,
    #         'color': 'Black',
    #         'price': 28000,
    #         'image': 'https://cdn2.riastatic.com/photosnew/auto/photo/bmw_4-series__511308392f.webp',
    #     }
    #     response = self.client.post(reverse("api:car-create"), data, format='json')
    #     self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_car_delete_view(self):
        self.client.force_authenticate(user=self.user)
        self.car = create_sample_car()
        response = self.client.delete(reverse("api:car-delete", kwargs={"pk": self.car.id}))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
