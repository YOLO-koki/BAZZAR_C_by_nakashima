from comp.forms import LoginCustomUserForm
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.urls import reverse_lazy

# ログイン機能


class CompLoginView(LoginView):
    template_name: str = 'comp/bo_login.html'
    form_class = LoginCustomUserForm
    success_url = reverse_lazy('comp:index')
