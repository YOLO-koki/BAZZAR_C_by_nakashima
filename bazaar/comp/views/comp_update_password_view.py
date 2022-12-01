from django.views.generic import TemplateView

class CompUpdatePasswordView(TemplateView):
    template_name: str = 'comp/bo_update_password.html'