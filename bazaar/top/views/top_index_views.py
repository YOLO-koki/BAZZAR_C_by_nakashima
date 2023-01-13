from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.db.models import Q
from comp.models import Store

# トップページview


class TopIndexView(ListView):
    model = Store
    template_name: str = "top/co_toppage.html"
    context_object_name = 'stores'

    # def get_queryset(self):
    #     queryset = Store.objects
    #     query = self.request.GET.get('query')

    #     if query:
    #         queryset = queryset.filter(
    #             Q(store_name = query) | Q(text__icontains = query)
    #         )

    #         return queryset
    
    def qobject(request):
        objects = Store.objects.filter(Q(store_name__contais="search"))
        return(Store.objects.all)