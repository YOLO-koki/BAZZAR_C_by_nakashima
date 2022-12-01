from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,DetailView
from django.urls import reverse_lazy

class CoStoreDetailView(DetailView):
    model = store
    template_name = "top/co_store_detail.html"