from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.db.models import Q
from comp.models import Store
import json

# トップページview


class TopIndexView(ListView):
    model = Store
    template_name: str = "top/co_toppage.html"
    context_object_name = 'stores'

    def get_queryset(self):
        queryset = Store.objects.all()
        query = self.request.GET.get('search')

        if query:
            queryset = queryset.filter(
                Q(store_name__contains = query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(list(Store.objects.values()))
        print(context['qs_json'])
        return context
