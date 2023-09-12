from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED)
from rest_framework.test import APIClient

from autoshipping.models import Car, Category
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

    def test_car_create_view(self):
        self.client.force_authenticate(user=self.user)
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        category = Category.objects.create(name="One")
        data = {
            'category': category.id,
            'name': 'Toyota Camry',
            'brand': 'Toyota',
            'model': 'Camry',
            'year': 2022,
            'description': 'Toyota Camry',
            'vin_code': 'JTNB11HK102345668',
            'mileage': 15000,
            'color': 'Black',
            'price': 28000,
        }
        files = {'image': ('test_image.jpg', image)}
        response = self.client.post(
            reverse("api:car-create"),
            data,
            format='multipart',
            files=files,
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_car_delete_view(self):
        self.client.force_authenticate(user=self.user)
        self.car = create_sample_car()
        response = self.client.delete(reverse("api:car-delete", kwargs={"pk": self.car.id}))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_car_update_view(self):
        self.client.force_authenticate(user=self.user)
        car = create_sample_car()
        new_data = {
            'name': 'Updated Camry',
            'year': 2023,
            'mileage': 20000,
        }
        response = self.client.patch(
            reverse("api:car-update", kwargs={"pk": car.id}),
            new_data,
            format='json',
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        updated_car = Car.objects.get(pk=car.id)
        self.assertEqual(updated_car.name, new_data['name'])
        self.assertEqual(updated_car.year, new_data['year'])
        self.assertEqual(updated_car.mileage, new_data['mileage'])

    def test_car_retrieve_view(self):
        self.client.force_authenticate(user=self.user)
        car = create_sample_car()
        response = self.client.get(reverse("api:car-detail", kwargs={"pk": car.id}))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['name'], car.name)
        self.assertEqual(response.data['year'], car.year)

    def test_unauthorized_user_view(self):
        response = self.client.get('/api/cars/create/')
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)
