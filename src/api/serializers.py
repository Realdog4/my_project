from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from account.models import User
from autoshipping.models import Car, Category, PriceList


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number')
        ref_name = 'MyUser'


class CarSerializer(ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Car
        fields = ('name', 'category', 'brand', 'model', 'year', 'description', 'vin_code', 'mileage', 'color', 'price',
                  'image')
