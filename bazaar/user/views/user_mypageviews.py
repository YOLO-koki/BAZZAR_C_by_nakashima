from django.shortcuts import render
from django.views.generic import TemplateView

class UserMypageView(TemplateView):
    template_name: str = "user/user_mypage.html"