from django.views.generic import TemplateView

class CompResetPasswordView(TemplateView):
    template_name: str = 'comp/bo_reset_password.html'