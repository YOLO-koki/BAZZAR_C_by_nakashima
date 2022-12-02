from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from comp.models import Store

# トップページview


class TopIndexView(TemplateView):
    template_name: str = "top/co_toppage.html"
    
    def search(request):
        objects = Store.objects.filter(Q(store_name__iexact="1") | Q(store_name__icontains="い"))
        return render(request,)