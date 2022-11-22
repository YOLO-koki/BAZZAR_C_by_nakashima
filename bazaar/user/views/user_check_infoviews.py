from django.views.generic import TemplateView
from django.shortcuts import render

class UserCheckView(TemplateView):

    template_name= 'user/user_check_registed_info.html'