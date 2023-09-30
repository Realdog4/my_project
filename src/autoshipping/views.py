from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from autoshipping.models import Car


class IndexView(TemplateView):
    template_name = "index.html"
    http_method_names = ['get']


class Custom404View(View):
    def get(self, request, exception=None):
        return render(request, '404.html', status=404)


class CarListView(ListView):
    model = Car
    template_name = "catalog/catalog_car.html"
    context_object_name = "car_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        search_fields = ["name", "brand", "model"]

        if search_query:
            or_filter = Q()
            for field in search_fields:
                or_filter |= Q(**{f"{field}__icontains": search_query})
            queryset = queryset.filter(or_filter)

        return queryset


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_details/car_details.html'
    context_object_name = 'details'
    pk_url_kwarg = "pk"
