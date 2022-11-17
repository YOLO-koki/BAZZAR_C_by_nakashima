from django.shortcuts import render
from django.views.generic import TemplateView

#トップページview
class UserIndexView(TemplateView):
    template_name: str = "layout/user/base.html"