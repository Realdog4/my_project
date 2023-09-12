from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from autoshipping.models import Car
from core.permissions import IsSuperUser

from .serializers import CarSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CarListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarCreateView(CreateAPIView):
    permission_classes = [IsSuperUser]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsSuperUser]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDeleteView(DestroyAPIView):
    permission_classes = [IsSuperUser]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
