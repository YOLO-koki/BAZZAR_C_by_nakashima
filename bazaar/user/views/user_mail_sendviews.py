from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class UserMailSendView(TemplateView):
    template_name= "user/user_mail_send.html"

    def __init__(self):
        self.params = {
        'user_id':'',
        'password':'',
        'name':'',
        'mail':'',
        'phone':'',
        }
    
    def post(self, request):
        user_id = request.POST["user_id"]
        password = request.POST["password"]
        name = request.POST["name"]
        mail = request.POST["mail"]
        phone = request.POST["phone"]
        self.params["user_id"] = user_id
        self.params["password"] = password
        self.params["name"] = name
        self.params["mail"] = mail
        self.params["phone"] = phone
        df = self.params

        return render(request, 'user/user_mail_send.html', df)