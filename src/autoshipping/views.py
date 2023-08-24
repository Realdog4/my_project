from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    http_method_names = ['get']


class Custom404View(View):
    def get(self, request, exception=None):
        return render(request, '404.html', status=404)
