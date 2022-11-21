from django.shortcuts import render
from django.views.generic import TemplateView

class CompMypageView(TemplateView):
    template_name: str = "comp/bo_mypage.html"