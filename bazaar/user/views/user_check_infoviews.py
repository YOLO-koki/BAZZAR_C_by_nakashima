from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from ..forms import RegisterForm
from accounts.models import CustomUser
from django.http.response import HttpResponseRedirect


from django.core.exceptions import ValidationError

class CheckRegiInfoView(CreateView):
    template_name="user/user_check_registed_info.html"
    model= CustomUser
    form_class = RegisterForm
    #success_url = reverse_lazy('user:userMailSend')

    def form_valid(self, form):
            user = form.save(commit=False)
            user.usertype = 'user'
            user.save()
            return redirect('user:userMailSend')
            

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     self.object = user
    #     return HttpResponseRedirect(self.get_success_url())

    
    
    # def __init__(self):
    #     self.params = {
    #     'userId':'',
    #     'password':'',
    #     'name':'',
    #     'mail':'',
    #     'phone':'',
    #     }
    
    # def post(self, request):
    #     user_id = request.POST["userid"]
    #     password = '*' * len(request.POST["password1"])
    #     name = request.POST["username"]
    #     mail = request.POST["mail"]
    #     phone = request.POST["phone"]
    #     self.params["user_id"] = user_id
    #     self.params["password"] = password
    #     self.params["name"] = name
    #     self.params["mail"] = mail
    #     self.params["phone"] = phone
    #     df = self.params
    #     return render(request, 'user/user_check_registed_info.html', df)