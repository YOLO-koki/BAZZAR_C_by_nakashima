from django.shortcuts import render
from django.views.generic import TemplateView #テンプレートタグ

# ログイン・ログアウト処理に利用
from django.contrib.auth.views import LogoutView



class Logout(LogoutView):
    template_name = 'logout.html'