from django.urls import path

from .views import CarDetailView, CarListView

app_name = "cars"

urlpatterns = [
    path("", CarListView.as_view(), name="car_list"),
    path("details/<int:pk>/", CarDetailView.as_view(), name="details"),
]
