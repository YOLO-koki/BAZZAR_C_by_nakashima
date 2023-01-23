from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,DetailView
from django.urls import reverse_lazy
from comp.models import Store,Kuchikomi


class CoStoreDetailView(DetailView):
    model = Store
    template_name = "top/co_store_detail.html"
    context_object_name = 'stores'

    def get_context_data(self, **kwargs):
        context = super(CoStoreDetailView,self).get_context_data(**kwargs)
        context.update({
            'kuchikomi_list':Kuchikomi.objects.all()
        })
        return context

    def get_queryset(self):
        return Store.objects.all()