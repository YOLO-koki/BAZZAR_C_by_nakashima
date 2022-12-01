from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from ..forms import MyPasswordResetForm

class PasswordReset(PasswordResetView):
    """パスワード変更用URLの送付ページ"""
    template_name = 'accounts/password_reset.html'
    subject_template_name = 'accounts/email/password_reset_subject.txt' #題名
    email_template_name = 'accounts/email/password_reset_message.txt' #内容
    
    form_class = MyPasswordResetForm
    success_url = reverse_lazy('accounts:password_reset_done')