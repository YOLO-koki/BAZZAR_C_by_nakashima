from django.shortcuts import render
from ..models import Store
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#ログインしていることが条件
class CustomPerfectView(LoginRequiredMixin, TemplateView):
    template_name = "comp/bo_custom_perfect.html"