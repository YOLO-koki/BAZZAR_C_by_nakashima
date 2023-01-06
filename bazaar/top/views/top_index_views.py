from django.shortcuts import render
from django.views.generic import ListView ,TemplateView
from django.db.models import Q
from comp.models import Store

# トップページview


class TopIndexView(ListView):
    model = Store
    template_name: str = "top/co_toppage.html"
    context_object_name = 'stores'

    # def store_list(request):
    #     template_name: str = "top/co_toppage.html"
    #     store = {}
    #     sl = Store.objects.all()
    #     store["objects_list"] = sl

    #     return render(request, template_name ,store)
    
    # def search(request):
    #     objects = Store.objects.filter(Q(store_name__iexact="1") | Q(store_name__icontains="い"))
    #     return render(request,)