from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from ..forms import RegisterForm

from django.core.exceptions import ValidationError

class CheckRegiInfoView(TemplateView):
    template_name = "user/user_check_registed_info.html"
    
    def __init__(self):
        self.params = {
        'userId':'',
        'password':'',
        'name':'',
        'mail':'',
        'phone':'',
        }
    
    def post(self, request):
        user_id = request.POST["userid"]
        password = '*' * len(request.POST["password1"])
        name = request.POST["username"]
        mail = request.POST["mail"]
        phone = request.POST["phone"]
        self.params["user_id"] = user_id
        self.params["password"] = password
        self.params["name"] = name
        self.params["mail"] = mail
        self.params["phone"] = phone
        df = self.params
        return render(request, 'user/user_check_registed_info.html', df)