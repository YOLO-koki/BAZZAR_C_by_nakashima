from django.views.generic import TemplateView

class UserRegistView(TemplateView):
    template_name= "user/user_create_account.html"