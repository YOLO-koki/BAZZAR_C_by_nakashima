from django.contrib.auth.views import LogoutView

class CompLogoutView(LogoutView):
    template_name: str = 'top/co_toppage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'ログアウトしました。'
        return context