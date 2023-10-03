from django.urls import path

from .views import CarDetailView, CarListView
from . import views

app_name = "cars"

urlpatterns = [
    path("", CarListView.as_view(), name="car_list"),
    path("details/<int:pk>/", CarDetailView.as_view(), name="details"),
    path('generate_category/', views.generate_category_view, name='generate_category'),
    path('create_sample_car/', views.create_sample_car_view, name='create_sample_car'),
    path('create_sample_delivery/', views.create_sample_delivery_view, name='create_sample_delivery'),
]
