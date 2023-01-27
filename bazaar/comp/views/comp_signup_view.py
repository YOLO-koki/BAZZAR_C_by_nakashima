from django.views.generic import TemplateView


# 新規登録
class CompSignupView(TemplateView):
    template_name: str = 'comp/bo_signup.html'
