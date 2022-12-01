from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView,View
from django.urls import reverse_lazy
from ..forms import RegisterForm
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse


class CreateAccountView(FormView):
    template_name = "comp/bo_create_account.html"
    form_class = RegisterForm
    success_url = reverse_lazy('comp:boCheck')
    def form_valid(self, form):
        return render(request=self.request,template_name="comp/bo_check_registed_info.html",context={'form':form})





    #success_url = reverse_lazy(("user_check_registed_info.html"))

    
