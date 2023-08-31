from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer, CarSerializer
from autoshipping.models import Car


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarCreateView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdateView(RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDeleteView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



