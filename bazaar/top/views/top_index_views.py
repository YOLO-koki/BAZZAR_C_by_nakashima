from django.shortcuts import render
from django.views.generic import TemplateView

# トップページview


class TopIndexView(TemplateView):
    template_name: str = "top/co_toppage.html"
