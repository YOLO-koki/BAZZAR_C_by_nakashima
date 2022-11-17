from django.shortcuts import render
from django.views.generic import TemplateView

#トップページview
class CompIndexView(TemplateView):
    template_name: str = "layout/comp/base.html"