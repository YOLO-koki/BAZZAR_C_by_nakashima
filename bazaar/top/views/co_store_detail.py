from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,DetailView
from django.urls import reverse_lazy
from comp.models import Store,Kuchikomi
from django.db.models import Avg
from django.db.models import Count


class CoStoreDetailView(DetailView):
    model = Store
    template_name = "top/co_store_detail.html"
    context_object_name = 'stores'

    def get_context_data(self,**kwargs):
        context = super(CoStoreDetailView,self).get_context_data(**kwargs)
        pk = kwargs['object'].pk
        avg_score = Kuchikomi.objects.filter(store_id_id = pk).aggregate(avg_score = Avg('score'))
        context.update({
            'kuchikomi_list':Kuchikomi.objects.all(),
            'avg_score':avg_score
        })
        return context

    def get_queryset(self):
        return Store.objects.all()