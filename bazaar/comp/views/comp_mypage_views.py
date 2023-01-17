from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CompMypageView(TemplateView):
    template_name = "comp/bo_mypage.html"