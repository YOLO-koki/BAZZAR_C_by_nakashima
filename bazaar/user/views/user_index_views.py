from django.shortcuts import render
from django.views.generic import TemplateView

#トップページview
class UserIndexView(TemplateView):
    template_name: str = "user/index.html"