from django.views.generic import TemplateView, FormView
from user.forms import LoginBusiness_personForm

# ログイン機能


class UserLoginView(FormView):
    template_name: str = 'user/user_login.html'
    form_class = LoginBusiness_personForm
    success_url = 'user:index'