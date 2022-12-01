from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy
from ..forms import MySetPasswordForm

class PasswordResetConfirm(PasswordResetConfirmView):
    """新パスワード入力ページ"""
    form_class = MySetPasswordForm
    success_url = reverse_lazy('accounts:password_reset_complete')
    template_name = 'accounts/password_reset_confirm.html'