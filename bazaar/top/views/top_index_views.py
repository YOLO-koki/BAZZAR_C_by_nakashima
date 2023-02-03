from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.db.models import Q
from comp.models import Store
import json
import re

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
        qs_json = json.dumps(list(Store.objects.values()), ensure_ascii=False)
        qs_json = re.sub(r"\\n", "", qs_json)
        qs_json = re.sub(r"\\r", "", qs_json)
        print(qs_json)
        context['qs_json'] = qs_json
        return context
