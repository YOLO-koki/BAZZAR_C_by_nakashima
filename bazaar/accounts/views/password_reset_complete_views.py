from django.contrib.auth.views import PasswordResetCompleteView

class PasswordResetComplete(PasswordResetCompleteView):
    """新パスワード設定しましたページ"""
    template_name = 'accounts/password_reset_complete.html'