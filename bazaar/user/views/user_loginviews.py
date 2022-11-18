from django.views.generic import TemplateView

class UserLoginView(TemplateView):
    template_name= "user/user_login.html"