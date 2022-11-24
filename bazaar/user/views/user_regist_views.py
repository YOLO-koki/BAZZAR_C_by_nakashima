from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from django.urls import reverse_lazy
from ..forms import RegisterForm

class CreateAccountView(FormView):
    template_name = "user/user_create_account.html"
    form_class = RegisterForm
    success_url = reverse_lazy('user/user_check_registed_info.html')