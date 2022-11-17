from django.views.generic import TemplateView

class UserCheckView(TemplateView):
    template_name= "user/user_check_registed_info.html"