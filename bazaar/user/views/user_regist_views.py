

# Create your views here.
from django.views.generic import FormView
from django.urls import reverse_lazy
from ..forms import RegisterForm
from ..models.users import User
from django.shortcuts import render

class CreateAccountView(FormView):
    template_name = "user/user_create_account.html"
    form_class = RegisterForm
    success_url = reverse_lazy('user:userCheck')
    def form_valid(self, form):
        return render(request=self.request,template_name="user/user_check_registed_info.html",context={'form':form})
      
