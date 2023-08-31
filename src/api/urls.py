from rest_framework import routers, permissions
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import UserViewSet, CarListView, CarCreateView, CarUpdateView, CarDeleteView

app_name = "api"
router = routers.DefaultRouter()
router.register('users', UserViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='swagger-docs'),
    path('cars/', CarListView.as_view(), name="cars_list"),
    path('cars/create/', CarCreateView.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
]