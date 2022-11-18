from django.views.generic import TemplateView, FormView
from comp.forms import LoginBusiness_personForm

# ログイン機能


class CompLoginView(FormView):
    template_name: str = 'comp/bo_login.html'
    form_class = LoginBusiness_personForm
    success_url = 'comp:index'
