from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.models import CustomUser

# トップページview


class TestView(TemplateView):
    model = CustomUser
    template_name: str = "top/test.html"
    pk_url_kwarg = 'userid'