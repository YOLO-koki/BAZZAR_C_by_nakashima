from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,DetailView
from django.urls import reverse_lazy
from comp.models import Store


class CoStoreDetailView(TemplateView):
    # model = Store
    template_name = "top/co_store_detail.html"
    # pk_url_kwarg = 'store_id'