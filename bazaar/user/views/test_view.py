from django.views.generic import TemplateView
from django.views.generic import FormView
class testview(FormView):

    template_name= "user/user_create_account.html"