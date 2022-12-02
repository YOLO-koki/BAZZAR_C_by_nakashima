from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#ログインしていることが条件
class CompMypageView(LoginRequiredMixin, TemplateView):
    template_name: str = "comp/bo_mypage.html"