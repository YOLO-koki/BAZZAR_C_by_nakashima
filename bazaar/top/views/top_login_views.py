from django.shortcuts import render
from django.views.generic import TemplateView

# トップページview


class TopLoginView(TemplateView):
    template_name: str = "top/top_login.html"
