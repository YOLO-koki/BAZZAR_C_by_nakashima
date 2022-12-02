from django.contrib.auth.views import LogoutView
from django.views.generic import FormView
from ..forms import LoginCustomUserForm

class CompLogoutView(LogoutView, FormView):
    template_name: str = 'comp/bo_login.html'
    form_class = LoginCustomUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'ログアウトしました。'
        return context