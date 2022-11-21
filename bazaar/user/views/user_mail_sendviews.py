from django.views.generic import TemplateView

class UserMailSendView(TemplateView):
    template_name= "user/user_mail_send.html"