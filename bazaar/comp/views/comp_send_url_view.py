from django.views.generic import TemplateView


# 新規登録確定URL送信
class CompSendURLView(TemplateView):
    template_name: str = 'comp/bo_send_url.html'
